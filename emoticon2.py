# -*- coding: utf-8 -*-
import re

def cleaner(tweet):
	"""convert the emoticons in the relative unicode"""
	clean_text = tweet
	
	clean_text = re.sub(r"(smile_angel|smile_surprise|smile_happy|smile_laugh|smile_kiss|smile_wink|smile_tongue_sticking_out)", " smile_positive ",clean_text)

	clean_text = re.sub(r"(smile_evil|smile_angry|smile_sad|smile_crying|smile_horror|smile_skeptical|smile_straight_face)"," smile_negative ",clean_text)

	return clean_text
