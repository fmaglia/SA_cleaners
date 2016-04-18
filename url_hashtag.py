# -*- coding: utf-8 -*-
import re

def cleaner(tweet):
	"""remove urls, hashtag and quotes"""
	clean_text = tweet
	
	clean_text = clean_text.replace("\t", " ").replace("\n", " ")
		
	clean_text = re.sub(r'"', "'", clean_text)

	#remove the url
	clean_text = re.sub(r"(http|https):\S+"," ", clean_text)
	
	#remove the url of twitter's pic
	clean_text = re.sub(r"pic.twitter.com\S+"," ", clean_text)
	
	#remove the hashtag
	clean_text = re.sub(r"#\S+"," ", clean_text)
	
	#remove the @ (mentions)
	clean_text = re.sub(r"@\S+"," ", clean_text)


	#remove the RT
	clean_text = re.sub(r"(RT )"," ", clean_text)

	# ultimo raffinamento
	# remove not ascii chars
	tmp = ''
	for c in clean_text:
		if ord(c) < 128: tmp += c
	clean_text = tmp
	
	return clean_text
