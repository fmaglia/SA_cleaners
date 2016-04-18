# -*- coding: utf-8 -*-
import re
import punctuation
import emoticon
import emoticon2
import url_hashtag
import negation
import dictionary
import slang
import sys
import insult
import final
import Tkinter
import csv
import os
from tkinter import filedialog
import tkFileDialog


#training set: 2016_gold_train + 2015_train_full
#test set: 2016_gold_dev o 2015_dev_gold


class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        
        self.file_path = filedialog.askopenfilename()
        #print "path: "+self.file_path
        
        label = Tkinter.Label(self,text="inserisci nome fileCleaned.tsv", padx = 20,font = "Arial 15 ").pack(anchor = "w")
        
        self.destFinale = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.destFinale, justify="center").pack(anchor="w")
        
        self.radio = Tkinter.IntVar()
        titolo = Tkinter.Label(self,  text="Scegli il tipo di elaborazione:", padx = 20,pady = 10,font = "Arial 15 ").pack(anchor="w")
        self.r1=Tkinter.Radiobutton(self, text="No preprocess", padx = 20,font = "Arial 15 ", variable=self.radio, value=1).pack(anchor = "w")
        self.r2=Tkinter.Radiobutton(self, text="Basic cleaner", padx = 20,font = "Arial 15 ", variable=self.radio, value=2).pack(anchor = "w")
        self.r3=Tkinter.Radiobutton(self, text="Basic + Dictionaries", padx = 20,font = "Arial 15 ", variable=self.radio, value=3).pack(anchor = "w")
        self.r4=Tkinter.Radiobutton(self, text="Basic + Negation", padx = 20,font = "Arial 15 ", variable=self.radio, value=4).pack(anchor = "w")
        self.r5=Tkinter.Radiobutton(self, text="Basic + 2-Emoticons", padx = 20,font = "Arial 15 ", variable=self.radio, value=5).pack(anchor = "w")
        self.r6=Tkinter.Radiobutton(self, text="All cleaners", padx = 20,font = "Arial 15 ", variable=self.radio, value=6).pack(anchor = "w")
        self.r7=Tkinter.Radiobutton(self, text="Full without dictionary", padx = 20,font = "Arial 15 ", variable=self.radio, value=7).pack(anchor = "w")
        
        #self.test = Tkinter.IntVar()
        #c = Tkinter.Checkbutton(self, text="Clicca se vuoi positive/negative in numero uguale", variable=self.test).pack()

        button = Tkinter.Button(self,text=u"esegui elaborazione",font = "Arial 15 ",command=self.OnButtonClick).pack(anchor="w")

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable, padx = 20,font = "Arial 15 ").pack(anchor = "w")

        self.resizable(True,False)
        self.update()

    def OnButtonClick(self):
        reload(sys)
        sys.setdefaultencoding('utf8')
        self.labelVariable.set( " You clicked the button: " + str(self.radio.get()))
        with open(self.destFinale.get(), 'w') as tsv_cleaned:
			writer = csv.writer(tsv_cleaned, delimiter='\t')
			#countPos = 0
			#countNeg = 0
			#with open(self.file_path,'r') as tsvfile: #file originale
				#tsvreader = csv.reader(tsvfile, delimiter="\t")
				#for line in tsvreader:
					#if (re.search(r'[0-9]{5,}', line[1])):
						##print "4 columns"
						#indice = 3
					#else:
						##print "3 columns"
						#indice = 2
					#if (line[indice-1]=="positive" and line[indice]!="Not Available" and re.search(r'(練|習|中|こ|れ|面|白|い|な|ｗ)',line[indice])==None):
						#countPos +=1
					#elif (line[indice-1]=="negative" and line[indice]!="Not Available" and re.search(r'(練|習|中|こ|れ|面|白|い|な|ｗ)',line[indice])==None):
						#countNeg +=1
					
				#print countPos
				#print countNeg	
				#print self.test.get()
				#if (self.test.get()==1):
					#if (countPos > countNeg):
						#countPos = countNeg
					#else:
						#countNeg = countPos
				
			with open(self.file_path,'r') as tsvfile: #file originale
				tsvreader = csv.reader(tsvfile, delimiter="\t")
				indice = 0
				for line in tsvreader:
					if (re.search(r'[0-9]{5,}', line[1])):
						#print "4 columns"
						indice = 3
					else:
						#print "3 columns"
						indice = 2
					if (re.search(r'(練|習|中|こ|れ|面|白|い|な|ｗ)',line[indice])==None and line[indice]!="Not Available"):
						if (self.radio.get()!=1):

							clean_text = line[indice].replace("\r", " ").replace("\n", " ").replace("\t", '').replace("\"", "")
							#if ((line[indice-1]=="positive" and countPos>0) or (line[indice-1]=="negative" and countNeg>0)):
							clean_text = url_hashtag.cleaner(clean_text)
							clean_text = emoticon.cleaner(clean_text)
							clean_text = punctuation.cleaner(clean_text)
							if (self.radio.get()==3):
								clean_text = slang.cleaner(clean_text)
								clean_text = dictionary.cleaner(clean_text)
								clean_text = insult.cleaner(clean_text)
							elif (self.radio.get()==4):
								clean_text = negation.cleaner(clean_text)
							elif (self.radio.get()==5):
								clean_text = emoticon2.cleaner(clean_text)
							elif (self.radio.get()==6):
								clean_text = slang.cleaner(clean_text)
								clean_text = dictionary.cleaner(clean_text)
								clean_text = insult.cleaner(clean_text)
								clean_text = emoticon2.cleaner(clean_text)
								clean_text = negation.cleaner(clean_text)
							elif (self.radio.get()==7):
								clean_text = slang.cleaner(clean_text)
								clean_text = insult.cleaner(clean_text)
								clean_text = emoticon2.cleaner(clean_text)
								clean_text = negation.cleaner(clean_text)
								
							clean_text = final.cleaner(clean_text)
						
								#if (line[indice-1]=="positive" and countPos>0):
									#print "pos: "+line[indice]
							writer.writerow([line[indice-1],clean_text])
									#countPos -=1
								#if (line[indice-1]=="negative" and countNeg>0):
									##print "neg: "+line[indice]
									#writer.writerow([line[indice-1],clean_text])
									#countNeg -=1
								#f2.write('"'+clean_text+'",'+line[indice-1]+"\n");
						else:
							#print "not cleaned"

							line[indice]=re.sub("\"", "'", line[indice])
							line[indice] = line[indice].replace("\t", " ").replace("\n", " ")

							#if (line[indice-1]=="positive" and countPos>0):
							writer.writerow([line[indice-1],line[indice]])
								#countPos -=1
							#if (line[indice-1]=="negative" and countNeg>0):
								#writer.writerow([line[indice-1],line[indice]])
								#countNeg -=1
						#f2.write('"'+line[indice]+'",'+line[indice-1]+"\n");
			print "Terminated"
			self.labelVariable.set( " Processing TERMINATED in "+self.destFinale.get())


if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Cleaner SemEval tweet')
    app.mainloop()
	
	
	

