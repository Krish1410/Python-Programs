import os
import argparse
import sys
from colorama import Fore,Back,Style,init
init(autoreset=True)
def cheak_in_file(filename,text):
    with open(filename,'r') as f:
        file_text=f.read()
    if text in file_text.lower():
        return True
    else:
        return False


def debuug():
    path=input(Fore.LIGHTCYAN_EX+"Enter The Folder Path Where Your Files is Exist :"+Fore.GREEN)
    os.chdir(path)
    files=os.listdir(path)
    found_text=[]
    nfound=0
    text=input(Fore.LIGHTCYAN_EX+"Enter The Text You Find in Files :"+Fore.GREEN)
    exe=input(Fore.LIGHTCYAN_EX+"Enter The File Name or Files Extenshion :"+Fore.GREEN)
    debuug=input(Fore.LIGHTCYAN_EX+"You See a back end prosees (y/n) :"+Fore.GREEN)
    if debuug is 'y':
        for file in files:
            if file.endswith(exe):
                print(f"Detecting in {Back.WHITE}{Fore.BLACK}{file}")
                flge=cheak_in_file(file,text)
                if flge==True:
                    print(f"{Style.DIM}{Fore.BLACK}{Back.GREEN}********{text}{Style.DIM} Found in{ file}********")
                    found_text.append(file)
                    nfound+=1
                else:
                    print(f'{Back.RED}{Fore.YELLOW} {text} IS NOT FOUND IN {file}')
                print(f"\033[31;1;4m{text}\033[0m Found in ({nfound}) files : {file}\n")
    else:
        for file in files:
            if file.endswith(exe):
                flge=cheak_in_file(file,text)
                if flge==True:
                    found_text.append(file)
                    nfound+=1
    print(f"{Fore.WHITE}{Back.GREEN}*{text} {Fore.YELLOW}{Back.RED}Find In Total ({nfound}) Files : ")
    Show=input(f"If you show a Files Name Where {text} is Find(y/n) :{Fore.GREEN}")
    if Show is 'y':
        print("\n".join(found_text[0:nfound]))
    else:
        print("Thanks For using This tool")
if __name__ == "__main__":
    os.system("cls")
    print(" 1.For Find a perticular Word or sentens \n")
    print(" 2.Play a snake Game \n")
    print(" 3.For Curancy converter \n")
    print(" 4.Play a stone Paper cizer Game \n")
    print(" 5.For open a calculater \n")
    print(" 6.For open a Tkinter Notpad \n")
    print(" 7.For Take a Sugeshion \n")
    opshion=int(input(" Enter Your Chois in Index Number"))
    if opshion==1:
        debuug()
    elif opshion==2:
        os.system("python K:\\python\\my_first.py")
    elif opshion==3:
        os.system("python K:\\python\\curancy.py")
    elif opshion==4:
        os.system("python K:\\python\\stonparercizer.py")
    elif opshion==5:
        os.system("python K:\\python\\calculater.py")
    elif opshion==6:
        os.system("python K:\\python\\notpad.py")
    elif opshion==7:
        os.system("python K:\\python\\sugeshion.py")
    else:
        print("You Enter a Wrong input or you are a exit ")
        exit()

    