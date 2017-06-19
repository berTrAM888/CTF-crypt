# /usr/bin/python27
#-*- coding:utf-8-*-
import hashlib

def md5(string):
	m=hashlib.md5()
	m=m.update(string)
	return m.hexdigest()
