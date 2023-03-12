import hashlib

hash_to_crack = input("Enter hash to crack:")
dict_name = input("Enter name of dictionary file:")

wordlist = open(dict_name,'r')

possible_pass = wordlist.readline()
while len(possible_pass) > 0:
    #print(possible_pass)
    possible_pass = possible_pass.strip()
    pass_hash = hashlib.md5()
    pass_hash.update(possible_pass.strip().encode())
    pass_hash = pass_hash.digest().hex()
    if pass_hash == hash_to_crack:
        print("PASSWORD FOUND:",possible_pass)
        break
    possible_pass = wordlist.readline()

'''
P.S. Figured out the error: There was an empty line in the rockyou.txt wordlist.
Running .strip() on an empty line made it so that the length of the possible_pass
string became zero prematurely. Due to this, the script broke out of the loop
before encountering the actual password.
I have changed the code now, so during the condition checking in the .strip()
function is only called after the condition checking in the while loop.
That way, the loop doesn't stop before its time.
'''
