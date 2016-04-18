# Tweepy
# Copyright 2009-2010 Joshua Roesslein
# See LICENSE for details.

"""
Tweepy Twitter API library
"""
__version__ = '0.1'
__author__ = 'Giulio Angiani'
__license__ = 'UNIPR'


import os
os.chdir("cleaners/")

__cleaners__ = [x.replace(".py", "") for x in os.listdir('.') if not x.startswith('__')]
os.chdir("../")

