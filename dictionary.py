# -*- coding: utf-8 -*-
import re
import enchant
import enchant.checker
from enchant.checker.CmdLineChecker import CmdLineChecker

def cleaner(tweet):
	"""correct the errors in the words mispelled"""
	clean_text = tweet	
	
	#better performance in time elaboration in opposition with the spellchecker of the textblob (0.32s vs 0.85s)
	from enchant.checker import SpellChecker
	chkr = SpellChecker("en_GB") #you can set "en_US" to use the us dictionary
	chkr.set_text(clean_text)
	#print clean_text
	for err in chkr:
		if (len(err.word)>3 and re.search(u'\u2019',err.word)==None):
			#print (err.word+" "+chkr.suggest(err.word)[0])
			text = err.word
			text = text.decode('latin-1')
			if isinstance(text, str):
				text = str(text.decode('ascii', 'ignore'))
			else:
				text = text.encode('ascii', 'ignore')
			err.replace_always(chkr.suggest(text)[0])
	
	clean_text = chkr.get_text()
	
	return clean_text
