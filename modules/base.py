#!/usr/bin/env python
# -*- coding:utf-8 -*-
import base64

	
def base_64(string,option):
	if option=="decode":
		return base64.b64decode(string)
	else:
		return base64.b64encode(string)

def base_32(string,option):
	if option=='decode':
		return base64.b32decode(string)
	else:
		return base64.b32encode(string)

def base_16(string,option):
	if option=='decode':
		return base64.b16decode(string)
	else:
		return base64.b16decode(string)
