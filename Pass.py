#Password Manager by Aman and Ayush
import os.path
import pyAesCrypt
import os
import sys
import time

#For encryption
bufferSize = 128 * 1024
crypto = input("Enter your master Password")

#Check if encrypted pw list is already created. If so, start decryption
def checkExistance():
    if os.path.exists("encryptedinfo.txt.aes"):
        checkPWD()
    else:
        appendNew()

# Menu
inp = str(input("Would you like to save a new password or view your old ones?"
                 "\n1. Input new password"
                 "\n2. View password"
                 "\n3. Exit"))
def appendNew():
    
    if (inp == '1'):

        file = open("info.txt", 'a')

        print()
        print()
        
        website = input("Enter Website: ")
        userName = input("Enter User Name: ")
        password = input("Enter Password: ")
        

        print()
        print()

        usrnm = "UserName: " + userName + "\n"
        pwd = "Password: " + password + "\n"
        web = "Website: " + website + "\n"

        file.write("---------------------------------------\n")
        file.write(usrnm)
        file.write(pwd)
        file.write(web)
        file.write("---------------------------------------\n")
        file.write("\n")
        file.close()
        readPasswords()
        
    elif (inp == '2'):
        readPasswords()
        sys.exit()
        
        
    elif (inp == '3'): 
        sys.exit()
    else:
        sys.exit()
        
        

#read passwords
def readPasswords():
    file = open("info.txt", 'r')
    content = file.read()
    file.close()
    print(content)

#re encrypt everything after you're finished
def encrypt():
    wait = input('Press ENTER to encrypt')
    pyAesCrypt.encryptFile("info.txt", "encryptedinfo.txt.aes", crypto, bufferSize)
    os.remove("info.txt")

#decrypt an AES file, this occurs if checkExistance found the AES
def decrypt():
    pyAesCrypt.decryptFile("encryptedinfo.txt.aes", "info.txt", crypto, bufferSize)

#checks if entered password matches decryption key. If not closes program
def checkPWD():
  pwd = str(input("Enter Your Master Password: "))
  if(pwd == crypto):
      decrypt()
  else: print("Incorrect"), time.sleep(2), sys.exit()


checkExistance()
appendNew()
encrypt()
