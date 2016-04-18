# -*- coding: utf-8 -*-
import re

def cleaner(tweet):
	"""remove punctuation repeated and introduce spaces between punctuation"""
	clean_text = tweet
	
	##convert 1 in ! if 1 is found between two !
	
	#clean_text = re.sub("!1+","!!",clean_text)
	#clean_text = re.sub("1+!","!!",clean_text)
	#clean_text = re.sub(r"1+\?","!?",clean_text)
	#clean_text = re.sub(r"\?1+","?!",clean_text)
	
	##print(clean_text)
	
	##add multistop tag when multiple punctuation signs are found
	#clean_text = re.sub(r"!!+"," multi_exclamation ",clean_text)
	#clean_text = re.sub(r"\?\?+"," multi_interrogation ",clean_text)
	#clean_text = re.sub(r"\.\.\.+"," multi_point ",clean_text)
	#clean_text = re.sub(r"(\?!)+"," multi_surprise ",clean_text)
	
	#clean the h in the laugh
	clean_text = re.sub('hh+', "h", clean_text)
	clean_text = re.sub('aaa+', "a", clean_text)
	clean_text = re.sub(r"(ah){2,}|(ha){2,}"," laught ",clean_text)
	
		#remove the punctuation
	clean_text = re.sub(r"(\.|,|:|;|\?|!|\)|\(|\-|\[|\]|\{|\}|\*|\||\<|\>|%|&|/|$|\+|@|#|\$|£|=|\^|~)"," ",clean_text)
	
	#introduce space between the words and the punctuation
	
	#clean_text = re.sub(r"\."," . ",clean_text)
	#clean_text = re.sub(r";"," ; ",clean_text)
	#clean_text = re.sub(r","," , ",clean_text)
	#clean_text = re.sub(r"!"," ! ",clean_text)
	#clean_text = re.sub(r"\?"," ? ",clean_text)
	#clean_text = re.sub(r":"," : ",clean_text)
	#clean_text = re.sub(r"\-"," - ",clean_text)
	#clean_text = re.sub(r"\("," ( ",clean_text)
	#clean_text = re.sub(r"\)"," ) ",clean_text)
	#clean_text = re.sub(r"\["," [ ",clean_text)	
	#clean_text = re.sub(r"\]"," ] ",clean_text)	
	#clean_text = re.sub(r"\{"," { ",clean_text)	
	#clean_text = re.sub(r"\}"," } ",clean_text)
	
	#remove the vowels repeated in sequence
	clean_text = re.sub("[a]{3,}","aa",clean_text)
	clean_text = re.sub("[e]{3,}","ee",clean_text)
	clean_text = re.sub("[i]{3,}","ii",clean_text)
	clean_text = re.sub("[o]{3,}","oo",clean_text)
	clean_text = re.sub("[u]{3,}","uu",clean_text)


	return clean_text
