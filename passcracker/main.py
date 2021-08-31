import hashlib

pass_hash = input("Enter md5 hash:") # input for hash to crack

wordlist = input("File name:") # the wordlist used to crack the hash

try:
    pass_file = open (wordlist, "r") # attempts to open and read the wordlist given
except:
    print("no file found") # prints this when the file is not found
    quit() # exits the program after file not found

for word in pass_file:
    enc_wrd = word.encode('utf-8') 
    digest = hashlib.md5(enc_wrd.strip()).hexdigest() # matches the hashes one by one

    if digest == pass_hash: # if the hash has been found it will do the following
        print("password has been found")
        print("password is "+ word)
        flag = 1
        break
if flag == 0: #if the password is not found
    print("password not found") 
