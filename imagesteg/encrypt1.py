from steganocryptopy.steganography import Steganography
n = input("What do you want to call your keys? :")
x = input("Path to file:")
f = input("What do you want to call the encrypted image?(remember to use .png):")
Steganography.generate_key(n)
encrypted = Steganography.encrypt(n, x, "pass.us") #remember to have a txt file with your hidden message
encrypted.save(f)
