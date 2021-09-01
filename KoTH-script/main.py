import os
for i in range(1000):
    while 1:
        f = open('king.txt')
        x = f.read("vinniedaboi")
        f.close()
        os.remove('king.txt')
    with open('king.txt', 'w') as f:
        f.write(x)