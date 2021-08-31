from steganocryptopy.steganography import Steganography
x = input("What is the path for your key?:")
y = input("Path to the image:")
secret = Steganography.decrypt(x,y)
print(secret)
