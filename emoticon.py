# -*- coding: utf-8 -*-
import re

def cleaner(tweet):
	"""convert the emoticons in the relative unicode"""
	clean_text = tweet
	

	#the list of emoticons and theirs convertion in unicode are found on Wikipedia
	
	#angel, innocent
	clean_text = re.sub(r"O:\-\)|0:\-3| 0:3 |0:\-\)|0:\)|0;\^\)"," smile_angel ",clean_text)
	#evil
	clean_text = re.sub(r">:\)|>;\)|>:\-\)|\}:\-\)|}:\)|3:\-\)|3:\)"," smile_evil ",clean_text)
	#happy
	clean_text = re.sub(r":\-\)|:\)|:D|:o\)|:\]| :3|:c\)|:>| =\]|8\)|=\)|:\}|:\^\)"," smile_happy ",clean_text)
	#laugh
	clean_text = re.sub(r":\-D|8\-D|8D|x\-D|xD|X\-D|XD|=\-D|=D|=\-3| =3 |B\^D|:\-\)\)|:'\-\)|:'\)"," smile_laugh ",clean_text)
	#angry
	clean_text = re.sub(r":\-\|\||:@| >:\("," smile_angry ",clean_text)
	#sad
	clean_text = re.sub(r">:\[|:\-\(|:\(|:\-c|:c|:\-<|:\-\[|:\[|:\{| <\\3 "," smile_sad " ,clean_text)
	#crying
	clean_text = re.sub(r";\(|:'\-\(|:'\("," smile_crying ",clean_text)
	#horror, disgust
	clean_text = re.sub(r"D:<|D:|D8| D; |D=|DX|v\.v|D\-':"," smile_horror ",clean_text)
	#surprise, shock
	clean_text = re.sub(r">:O|:\-O|:O|:\-o|:o|8\-0|O_O|o\-o|O_o|o_O|o_o|O\-O"," smile_surprise ",clean_text)
	#kiss
	clean_text = re.sub(r":\*|:\-\*|:\^\*|\( '\}\{' \)|<3"," smile_kiss ",clean_text)
	#winking
	clean_text = re.sub(r";\-\)|;\)|\*\-\)|\*\)|;\-\]|;\]|;D|;\^\)|:\-,"," smile_wink ",clean_text)
	#tongue sticking out
	clean_text = re.sub(r">:P|:\-P|:P|X\-P|x\-p| xp | XP |:\-p| :p | =p |:\-Þ|:Þ|:þ|:\-þ|:\-b| :b | d: "," smile_tongue_sticking_out ",clean_text)
	#skeptical
	clean_text = re.sub(r">:\\|>:/|:\-/|:\-\.|:/|:\\|=/|=\\| :L | =L | :S |>\.<"," smile_skeptical ",clean_text)
	#straight face
	clean_text = re.sub(r":\||:\-\|"," smile_straight_face ",clean_text)
	


	return clean_text
