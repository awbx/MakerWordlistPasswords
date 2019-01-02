'''
 The Script By Awbx King
'''
class bcolors:			#class colors 
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:
	import itertools
except ImportError as error:
	print(error,bcolors.WARNING,"=> You Must Install 'Itertools' !",bcolors.ENDC)
try:
	import re
except ImportError as error:
	print(error,bcolors.WARNING,"=> You Must Install 'Re' !",bcolors.ENDC)
import os,time
os.system('clear && clear')
print(bcolors.HEADER,bcolors.BOLD,"""
			===================================
			= The Maker Wordlist Passwords :) =
			===================================
			\r
			      The Script By Awbx King
			  \r
			          Fb:awbx.king.9
	""",bcolors.ENDC)
def make_wordlist(*args): #function make wordlist
	
	word     = args[0] 
	repeat   = args[1]
	save 	 = args[2]
	time 	 = args[3]	
	wordlist = itertools.product(word,repeat=repeat)
	myfile   = os.path.exists('wordlist/')
	'''if myfile == True :
		return 1
	else :
		os.mkdir('wordlist')
	'''
	file	 = open('wordlist/%s.txt'% save,'w+')
	file 	 = open(file.name,'r+')
	try:
		for j in wordlist :
			i = ''.join(j)+'\r'
			file.write(re.sub(r'',r'',i))
	except FileNotFoundError:
		print(bcolors.FAIL,'Wordlist Directory Is Not Found !',bcolors.ENDC)
	except KeyboardInterrupt:
		print(bcolors.OKBLUE,'Good Bey ^_o',bcolors.ENDC)
	file.close() 
try:
	
	lists	= input('Enter a Value Or Characters For Make Wordlist :')
	print('\n')
	repeat 	= int(input('Enter To Length The Password  Word [exmple:4,8,16]:'))
	print('\n')
	save  	= input('Enter Name For Save !:')
	print('\n')
	if lists != "" and save != "":
		print('Please Wait...')
		make_wordlist(lists,repeat,save,time)
		
		time.sleep(4)
		print(bcolors.OKGREEN,bcolors.BOLD,'File Save On wordlist/%s.txt'%(save),bcolors.ENDC)
	else:
		print(bcolors.FAIL,'\n Some Input Is Null Try Again ! \n',bcolors.ENDC)	
except EOFError  :
	print(bcolors.OKBLUE,'\n Good Bey ^_o \n',bcolors.ENDC)
except KeyboardInterrupt :
	print(bcolors.OKBLUE,'\n Good Bey ^_o\n ',bcolors.ENDC)
except NameError :
		print('')
except ValueError:
	print(bcolors.FAIL,'\n You Should Enetr Number Only ! Try Again :( \n',bcolors.ENDC)

