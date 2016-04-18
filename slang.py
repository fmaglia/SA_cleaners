# -*- coding: utf-8 -*-
import re
from nltk.tokenize import TweetTokenizer

def cleaner(tweet):
	"""convert slang in common words"""
	text = " " + tweet + " "
	t2 = TweetTokenizer()
	
	f = open("acronyms.txt","r")
	while 1:
		line = f.readline()
		if line=="":
			break
		
		token = t2.tokenize(line)				
		text = re.sub(" "+token[0]+" "," "+token[1]+" ",text)
		#print text
	f.close()
			
	return text





