# /usr/bin/python27
# -*- coding:utf-8 -*-
import sys
from optparse import OptionParser
import traceback
from modules import base
from modules.fence import fence_crypt
from modules.html import html_crypt
from modules.md import md5_encode
from modules.morse import morse_crypt
from modules.url import url_crypt
from modules.caesar import caesar_crypt


def print_banner():
	print "test"

def get_opt():
	usage = "usage: %prog [options] <args>"  
	parser=OptionParser(usage=usage)
	parser.add_option("-c","--crypt",help="choose crypt module",dest="crypt_module",metavar="crypt_module")
	parser.add_option("-s","--string",help="input your string you wanna encrypt or decrypt",dest="crypt_string",metavar="crypt_string")
	parser.add_option("-o","--option",help="input your option to this string <decode/encode>",dest="crypt_option",metavar="crypt_option")
	parser.add_option("-w","--splitword",help="input your split word for morse crypt",dest="split_word",metavar="split_word")
	(options, args) = parser.parse_args()
	return options
def main():
	print_banner()
	options=get_opt()
	if options.crypt_module[:4]=='base':
		if options.crypt_string== None or options.crypt_option== None:
			print "Parameter missing"
			print "Please input -h/--help to see how to use it"
			sys.exit()
		elif options.crypt_option != 'encode' and options.crypt_option!='decode':
			print "Parameter error"
			print "please input -h/--help to see how to use it"
			sys.exit()
		else:
			exec("print "+options.crypt_module[:4]+'.'+options.crypt_module[:4]+'_'+options.crypt_module[4:]+"('"+options.crypt_string+"','"+options.crypt_option+"')")
	elif options.crypt_module=='caesar':
		if options.crypt_string==None:
			print "Parameter missing"
			print "Please input -h/--help to see how to use it"
			sys.exit()
		else:
			caesar_crypt(options.crypt_string)
	elif options.crypt_module=='html':
		if options.crypt_option==None:
			print "Parameter missing"
			print "Please input -h/--help to see how to use it" 
			sys.exit()
		else:
			print html_crypt(options.crypt_string,options.crypt_option)
	elif options.crypt_module=='fence':
		if options.crypt_string==None:
			print "Parameter missing"
			print "Please input -h/--help to see how to use it"
			sys.exit()
		else:
			fence_crypt(options.crypt_string)
	elif  options.crypt_module=='morse':
		if options.crypt_string==None or options.crypt_option == None or options.split_word == None:
			print "Parameter missing"
			print "Please input -h/--help to see how to use it"
			sys.exit()
		else:
			print morse_crypt(options.crypt_string,options.crypt_option,options.split_word)
	elif options.crypt_module == 'url':
		if options.crypt_string==None or options.crypt_option==None:
			print "Parameter missing"
			print "Please input -h/--help to see how to use it"
			sys.exit()
		else:
			print url_crypt(options.crypt_string,options.crypt_option)	
if __name__=='__main__':
	main()
