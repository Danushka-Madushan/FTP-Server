from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from msvcrt import getch
from tkinter import Tk
from tkinter import *
from tkinter.filedialog import askdirectory
import base64
import json
import random
import string
import socket
import os
from time import sleep
import sys


os.system("COLOR A")
os.system("CLS")


root = Tk()
root.withdraw()


Banner = r'''

  █████▒▄▄▄█████▓ ██▓███       ██████ ▓█████  ██▀███   ██▒   █▓▓█████  ██▀███
▓██   ▒ ▓  ██▒ ▓▒▓██░  ██▒   ▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒████ ░ ▒ ▓██░ ▒░▓██░ ██▓▒   ░ ▓██▄   ▒███   ▓██ ░▄█ ▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█▒  ░ ░ ▓██▓ ░ ▒██▄█▓▒ ▒     ▒   ██▒▒▓█  ▄ ▒██▀▀█▄    ▒██ █░░▒▓█  ▄ ▒██▀▀█▄
░▒█░      ▒██▒ ░ ▒██▒ ░  ░   ▒██████▒▒░▒████▒░██▓ ▒██▒   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ▒ ░      ▒ ░░   ▒▓▒░ ░  ░   ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
 ░          ░    ░▒ ░        ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░   ░ ░░   ░ ░  ░  ░▒ ░ ▒░
 ░ ░      ░      ░░          ░  ░  ░     ░     ░░   ░      ░░     ░     ░░   ░
                                   ░     ░  ░   ░           ░     ░  ░   ░
                                        [V.2.0]  [Github.com/Danushka-Madushan]

'''
print(Banner)

OPTION = r'''
(01) Start File Transfer Protocol (Anonymous Mode)

(02) Start File Transfer Protocol (Protected Mode)

(03) Change Password

>>  '''
while(True):
    try:
        os.system("CLS")
        print(Banner)
        USER_CHOICE = int(input(OPTION))
        if USER_CHOICE == 1:
            while (True):
                try:
                    os.system("CLS")
                    print(Banner)
                    Authorizer = DummyAuthorizer()
                    USERNAME = socket.gethostname()
                    HOST_IP = socket.gethostbyname(USERNAME)
                    if HOST_IP == "127.0.0.1":
                        print(">> Please Connect to Network Before Start FTP...")
                        sleep(2)
                        sys.exit()
                    PORT = 8000
                    HOST = (HOST_IP, PORT)

                    print(">> Starting FTP...")
                    sleep(1)

                    HOME = askdirectory(title='Selct Hosting Folder...')
                    if HOME == "":
                        print(">> FTP Server Terminating...(No Folder Choosed!)")
                        sleep(3)
                        sys.exit()
                    Authorizer.add_anonymous(HOME, perm="elr")

                    print(f">> SERVER HOSTED LOCATION         : [ {HOME} ]")
                    print(
                        f">> FTP SERVER ADDRESS             : ftp://{HOST_IP}:{PORT}")
                    print("\n>> Server Started...")
                    Handler = FTPHandler
                    Handler.authorizer = Authorizer
                    Server = FTPServer(HOST, Handler)
                    Server.serve_forever()

                except KeyboardInterrupt:
                    print("\n\n>> Server Terminated...")
                    sleep(2)
                    break

                except Exception as E:
                    print(E)
                    print(">> Server Terminated...")
                    sleep(2)
                    break

        if USER_CHOICE == 2:
            while (True):
                try:
                    os.system("cls")
                    print(Banner)
                    Authorizer = DummyAuthorizer()
                    USERNAME = socket.gethostname()
                    HOST_IP = socket.gethostbyname(USERNAME)
                    if HOST_IP == "127.0.0.1":
                        print(">> Please Connect to Network Before Start FTP...")
                        sleep(2)
                        sys.exit()
                    else:
                        pass
                    PORT = 8000
                    HOST = (HOST_IP, PORT)

                    try:
                        Settings = open("Assets/settings.json", "r")
                    except Exception:
                        print(
                            ">> System Resource File Crashed! Please Select Option 3 in Main Menue.")
                        getch()
                        break

                    DATA = json.load(Settings)
                    PASSKEY = DATA['PASSKEY']

                    print(">> Starting FTP...")
                    sleep(1)

                    HOME = askdirectory(title='Selct Hosting Folder...')

                    if HOME == "":
                        print(">> FTP Server Terminating...(No Folder Choosed!)")
                        sleep(3)
                        sys.exit()
                    Authorizer.add_user(USERNAME, PASSKEY, HOME, perm="elradfmw",
                                        msg_login=f"Successfully Logged in to {USERNAME}", msg_quit="Have a Nice Day...")

                    print(
                        f">> LOGIN INFORMATION : USERNAME   : {USERNAME}")
                    print(f">> LOGIN INFORMATION : PASSWORD   : {PASSKEY}")
                    print(
                        f">> SERVER HOSTED LOCATION         : [ {HOME} ]")
                    print(
                        f">> FTP SERVER ADDRESS             : ftp://{HOST_IP}:{PORT}")

                    print("\n>> Server Started...\n\n")
                    Handler = FTPHandler
                    Handler.authorizer = Authorizer
                    Server = FTPServer(HOST, Handler)
                    Server.serve_forever()

                except KeyboardInterrupt:
                    print("\n\n>> Server Terminated...")
                    sleep(2)
                    break

                except Exception as E:
                    print(E)
                    print(">> Server Terminated...")
                    sleep(2)
                    break
        if USER_CHOICE == 3:
            while (True):
                os.system("cls")
                print(Banner)
                try:
                    Settings = open("Assets/settings.json", "r")
                    break
                except Exception:
                    message = ("CrYpTo2x")
                    message_bytes = message.encode('ascii')
                    base64_bytes = base64.b64encode(message_bytes)
                    base64_message = base64_bytes.decode('ascii')

                    PROTECTED_DATA = {
                        "PASSKEY": f"{message}",
                        "UNIQUE_KEY": f"{base64_message}"
                    }

                    PREFERENCES = json.dumps(PROTECTED_DATA, indent=2)

                    with open("Assets/settings.json", "w") as SETTINGS:
                        SETTINGS.write(PREFERENCES)
                        continue

            DATA = json.load(Settings)

            PASSWORD = DATA['PASSKEY']

            base64_message = DATA['UNIQUE_KEY']
            base64_bytes = base64_message.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            MESSAGE = message_bytes.decode('ascii')

            if PASSWORD == MESSAGE and MESSAGE == PASSWORD:
                print(">> Previous Data Authentication Sucessful!\n")
                while (True):
                    X = input(">> Enter New Password    : ")
                    if len(X) >= 8 and len(X) <= 16:
                        message = (X)
                        message_bytes = message.encode('ascii')
                        base64_bytes = base64.b64encode(message_bytes)
                        base64_message = base64_bytes.decode('ascii')

                        PROTECTED_DATA = {
                            "PASSKEY": f"{message}",
                            "UNIQUE_KEY": f"{base64_message}"
                        }

                        PREFERENCES = json.dumps(PROTECTED_DATA, indent=2)

                        with open("Assets/settings.json", "w") as SETTINGS:
                            SETTINGS.write(PREFERENCES)

                        print(f">> Your New Password is  : {X}\n")
                        print(">> Setting Sucessful..")
                        getch()
                        break
                    else:
                        print(
                            ">> Password Length Must Be Between 8 - 16 Characters !")
                        continue
            else:
                while (True):
                    os.system("cls")
                    print(Banner)
                    print(">> Previous Data Did not Match!!")
                    try:
                        OPTION = int(
                            input(">> To Reset this Applicaion Enter [1] Enter [0] For Exit : "))
                        if OPTION not in (0, 1):
                            continue
                        if OPTION == 1:
                            break
                        else:
                            sys.exit()
                    except ValueError:
                        continue

                message = ("CrYpTo2x")
                message_bytes = message.encode('ascii')
                base64_bytes = base64.b64encode(message_bytes)
                base64_message = base64_bytes.decode('ascii')

                PROTECTED_DATA = {
                    "PASSKEY": f"{message}",
                    "UNIQUE_KEY": f"{base64_message}"
                }

                PREFERENCES = json.dumps(PROTECTED_DATA, indent=2)

                with open("Assets/settings.json", "w") as SETTINGS:
                    SETTINGS.write(PREFERENCES)

                print(">> Password Reset Successful!")
                getch()
    except ValueError as E:
        print(E)
        print(">> Invalid Option....")
        sleep(1)
        getch()
        continue

    except KeyboardInterrupt:
        print("\n\n>> Server Terminated...")
        sleep(2)
        break
