# -*- coding: utf-8 -*-
import re

def cleaner(tweet):
	"""convert negative verbs in not"""
	clean_text = tweet
	
	
	#substitute the negation with a simple "not"
	
	clean_text = re.sub(r"isn't"," not ",clean_text)
	clean_text = re.sub(r"aren't"," not ",clean_text)
	clean_text = re.sub(r"don't"," not ",clean_text)
	clean_text = re.sub(r"didn't"," not ",clean_text)
	clean_text = re.sub(r"doesn't"," not ",clean_text)
	clean_text = re.sub(r"haven't"," not ",clean_text)
	clean_text = re.sub(r"hasn't"," not ",clean_text)
	clean_text = re.sub(r"wasn't"," not ",clean_text)
	clean_text = re.sub(r"weren't"," not ",clean_text)	
	clean_text = re.sub(r"won't"," not ",clean_text)
	clean_text = re.sub(r"never"," not ",clean_text)	
	clean_text = re.sub(r"can't"," not ",clean_text)
	clean_text = re.sub(r"cannot"," not ",clean_text)
	clean_text = re.sub(r"couldn't"," not ",clean_text)
	clean_text = re.sub(r"wouldn't"," not ",clean_text)
	clean_text = re.sub(r"shouldn't"," not ",clean_text)	


	return clean_text
