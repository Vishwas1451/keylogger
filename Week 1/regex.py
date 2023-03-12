#Importing the library here
import re

'''
    This function takes in a file object.
    A file object is the one you get when you
    call the open() function.
    f = open('sample.txt','r')
    f is a file object.
'''
def match_regex(file_object):
    #In this step, we read the contents of the file referenced by
    #file_object into the variable text
    text = file_object.read()
    #The next step is to create a regex to match the stuff we want.
    #This is the regex that matches an IP address. Type it out on regexr.com to get a
    #detailed explanation
    regex_IP = r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})'
    #This regex matches emails
    regex_email = r'([\w\.-]+@+[\w\.-]+\.+[\w]{1,5})'

    #Now, we match our text with these regular expressions.
    IP_matches = re.findall(regex_IP,text)
    email_matches = re.findall(regex_email,text)

    #re.findall: This function takes a regex and a string as arguments.
    #            It returns any matches of the regex found in the string
    #            A list of all matching substrings is returned.
    #            So, if there are no matches, an empty list is returned.
    #re.search: This is another interesting function. It does the same thing
    #           as re.findall(), but it only returns the first match, and that
    #           as a Match object.
    #           The Match object has three functions:
    #           .span() ==> Returns the starting and ending index of the match in
    #           the text
    #           .string ==> Returns the string passed to the function
    #           .group() ==> Returns only the part of the string that matches the regex

    #Now, we print the data we found
    for i in IP_matches:
    	print(i)

    for e in email_matches:
        print(e)

#Now that the function definition is done, we can call it.
#First, let's create a file object to pass to the function:
f = open('file_name.txt','r')
#Then, let's call the function match_regex with f as argument
match_regex(f)
#The function will run its course, print all the data found.
#Finally, before finishing, we close the file file_object
f.close()
