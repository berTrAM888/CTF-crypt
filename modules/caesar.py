#!/usr/bin/env python
# -*- coding:utf-8 -*-
import string
def caesar_crypt(strings):
    for i in range(26) :
        table = string.maketrans(string.ascii_lowercase + string.ascii_uppercase, string.ascii_lowercase[i:] + string.ascii_lowercase[:i] + string.ascii_uppercase[i:] + string.ascii_uppercase[:i])
        print strings.translate(table)  
