#!/usr/bin/env python
# -*-coding:utf-8-*-
import HTMLParser
import cgi

def html_crypt(string,option):
	if option=='decode':
		return HTMLParser.HTMLParser().unescape(string)
	else:
		return cgi.escape(string)
