#import the library
import requests

#requests.get sends a get request to the url specified in the argument.
#The response from the server is stored in the variable r.
r = requests.get('https://google.com')

#You can access the status code using r.status_code
print("STATUS CODE:",r.status_code)

#You can access all headers using r.headers. It's a dictionary
print(r.headers)

#Since r.headers is a dictionary, you can access one specific header as shown.
print("SERVER:",r.headers['Server'])
