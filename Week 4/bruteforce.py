import hashlib

small = list(chr(i) for i in range(ord('a'),ord('z')+1))
caps = list(chr(i) for i in range(ord('A'),ord('Z')+1))
numbers = list(str(i) for i in range(10))
#special_chars = ['@','#',...]
l = []
l.extend(small)
l.extend(caps)
l.extend(numbers)
l.append('')

hash = input("Enter the hash to crack:")
for n in l:
    for i in l:
      for j in l:
        for k in l:
          for m in l:
            passwd = n+i+j+k+m
            pass_hash = hashlib.md5()
            pass_hash.update(passwd.encode())
            hashed_pass = pass_hash.digest().hex()
            if hashed_pass == hash:
                print("Password found:",passwd)
                exit()
