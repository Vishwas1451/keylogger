import requests

base_URL = ""
dictionary_file_path = ""
dictionary_file = open(dictionary_file_path,'r')

while (True):
    directory = dictionary_file.readline().strip()
    if len(directory) == 0:
        break
    URI = base_URL + / + directory
    r = requests.get(URI)
    if r.status_code != 404:
        print("FOUND:",str(r.status_code),":",URI)
