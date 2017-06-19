#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

def morse_crypt(string,option,split_word=''):
	if option=='encode':
		CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
             'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }
		return_string=''
		string=left_words(string)
		for char in string:
			 return_string=return_string+CODE[char.upper()]+' '
		return return_string
	else:
		CODE = {
         '.-' : 'A',     '-...': 'B',   '-.-.': 'C',
         '-..': 'D',    '.': 'E',      '..-.': 'F',
         '--.': 'G',    '....': 'H',   '..': 'I',
         '.---': 'J',   '-.-': 'K',    '.-..': 'L',
         '--': 'M',     '-.': 'N',     '---': 'O',
         '.--.': 'P',   '--.-': 'Q',   '.-.': 'R',
         '...': 'S',    '-': 'T',      '..-': 'U',
         '...-': 'V',   '.--': 'W',    '-..-': 'X',
         '-.--': 'Y',   '--..': 'Z',
         '-----': '0',  '.----': '1',  '..---': '2',
         '...--': '3',  '....-': '4',  '.....': '5',
         '-....': '6',  '--...': '7',  '---..': '8',
         '----.': '9'
         }
		return_string=''
		string=string.split(split_word)
		for char in string:
			return_string=return_string+CODE[char]
		return return_string

def left_words(string):
	words=re.findall('[a-zA-Z0-9]+',string)
	return ''.join(words)
