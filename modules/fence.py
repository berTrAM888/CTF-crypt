#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

def fence_crypt(string,option='decode',num=1):
	if option=='encode':
		string=left_words(string)
	else:
		fence_decrypt(string)

def fence_decrypt(e):
    elen = len(e)
    field=[]
    for i in range(2,elen):
        if(elen%i==0):
            field.append(i)

    for f in field:
        b = elen / f
        result = {x:'' for x in range(b)}
        for i in range(elen):
            a = i % b;
            result.update({a:result[a] + e[i]})
        d = ''
        for i in range(b):
            d = d + result[i]
        print d.lower()
		

def left_words(string):
	return ''.join(re.findall('[a-zA-Z0-9]+',string))
