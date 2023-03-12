'''
	This library gives us access to various
	operating system interfaces through Python
	use os.system('<command>') to run that command
	on the terminal/command prompt.
	In this case, we'll use it to traverse directories
'''
import os

'''
	Regex library
'''
import re

#os.walk(path) --> pwd, subdirs, files [GENERATOR]

#FILE PATH: Linux: / EX: /root/home/Desktop/		Windows: \	C:\User\
'''
This function takes in a 'path', that's the location
of the folder you want to search.
It then searches that folder recursively,
searches folders within folders within folders...
and opens every file inside every folder inside
the folder you gave as argument.
'''
def iterative_travel(path):
	'''
	os.walk()
	'''
	for root, subdirs, files in os.walk(path):
		#print(root)
		#print(subdirs)
		#print(files)
		#print(type(root),type(subdirs),type(files))
		#print('----------------------------------')
		for i in files:
			f = open(root+'\\'+i)
			#Do something with the files
			find_matches(f)
			f.close()

def find_matches(file_object, email_flag=True, IP_flag = True):
	#file = open(file_name,'r')
	file = file_object
	text = file.read()
	regex_IP= r'([\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3})'
	#				\d -> digit 	[\d]{1,3} => Take any digit from 0-9, min 1 or max 3 times
	#				. -> special character	\. => Match for a '.'
	#				111.34.5.255
	regex_email = r'([\w\.-]@[\w.-]+\.+[\w]{1,5})'
	#				\w -> a-zA-Z	@ \w . -		.com .edu...
	#regex_url = r'((ftp|http|https):\/\/)?(www.)?(?!.*(ftp|http|https|www.))[a-zA-Z0-9_-]+(\.[a-zA-Z]+)+((\/)[\w#]+)*(\/\w+\?[a-zA-Z0-9_]+=\w+)*)?$/gm'		#Anything preceding a question mark is optional
	if IP_flag == True:
		IP_matches =  re.findall(regex_IP, text)
	if email_flag == True:
		email_matches =  re.findall(regex_email, text)
	#if url_flag == True:
	#	url_matches =  re.findall(regex_url, text)
	if len(IP_matches) > 0:
		print("IP ADDRESSES FOUND:")
		for match in IP_matches:
			print(match)
	if len(email_matches) > 0:
		print("EMAIL ADDRESSES FOUND:")
		for match in email_matches:
			print(match)
	#print("URLs ADDRESSES FOUND:")
	#for match in url_matches:
	#	print(match)


path = input("Enter Path: ")
iterative_travel(path)

'''
pass.txt	Lab_stuff
filepath = ./Desktop/pass.txt
filepath = ./Desktop/Lab_stuff

'''

'''
JWT
PASS Hashes --> Week3

PESUIO{<SRN>}

'''
