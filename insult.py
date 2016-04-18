# -*- coding: utf-8 -*-
import re
from nltk.tokenize import TweetTokenizer

def cleaner(tweet):
	"""convert the insults in bad_word"""
	text = tweet
	t2 = TweetTokenizer()
	f = open("insults.txt","r")
	while 1:
		line = f.readline()
		
		if line=="":
			break
		token = t2.tokenize(line)
		word = ""
		for w in token:
			word+=w+" "				
		text = re.sub(word," bad_word ",text)
	
	f.close()
			
	return text





