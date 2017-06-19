#!/usr/bin/env python
#-*- coding:utf-8-*-
import hashlib

def md5_encode(string):
	m=hashlib.md5()
	m.update(string)
	return m.hexdigest()
