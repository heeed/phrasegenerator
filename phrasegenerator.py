#!/usr/bin/env python
# 
#
#       ***phrasegenerator.py***
#
#	A simple python based phrase generator.
#	Inspired by a cheeky little script created by Les Pounder (@biglesp)
#       
#	Each list needs to be in a csv format
#       eg: adj.txt -> "a gigantic","a complete","the best"   etc etc 	
#       
#	Copyright 2013 michael rimicans (@heeedt)
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>
#

import csv
from random import choice

phraseAdjective = 'adj.txt'
phraseNoun = 'noun.txt'
phraseStart = 'intro.txt'

def getWords(nameFile):
	ins = open( nameFile, "rb" )
	wordArray = []
	line= csv.reader(ins,delimiter=',')
	for line2 in line:
		for word in line2:
			wordArray.append(word)
	ins.close()		
	return wordArray
	
def message():
	adj = getWords(phraseAdjective)
	noun = getWords(phraseNoun)
	intro =getWords(phraseStart)
	phrase = choice(intro)+choice(adj)+" "+choice(noun)
	return phrase


print message()
