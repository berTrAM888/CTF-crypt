#!/usr/bin/env python
# -*- coding:utf-8 -*-
from urllib import quote
from urllib import unquote

def url_crypt(string,option):
	if option=='decode':
		return unquote(string)
	else:
		return quote(string)
