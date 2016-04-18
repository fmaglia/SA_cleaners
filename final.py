# -*- coding: utf-8 -*-
import re

def cleaner(tweet):
	"""final step of cleaning"""
	clean_text = tweet
	
	clean_text = clean_text.lower()
		
	#normalize the space
	
	clean_text = re.sub(r"[ ]+"," ",clean_text)
	clean_text=clean_text.strip()
	return clean_text
