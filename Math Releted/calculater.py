#this is my claculater
# import squr
import pyttsx3
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def calcy():
    if __name__ == "__main__":
        print("you can enter only two number in this claculater")
        print("enter the first number")
        a=int(input())
        print("Enter the second number")
        b=int(input())
        print("\n")
        print(" \tfor minese(-) ")
        print(" \t fou pluse(+) ")
        print(" \t for divid(/) ")
        print(" \tfor multipal(*) ")
        print("choos any opreter in below")
        c=input()

        print("you choos a ",c)
        if c=='-':
            print("your ans is \n",a-b)
        elif c=='+':
            print("your ans is\n",a+b)
        elif c=='/':
            print("your ans is\n",a/b)
        elif c=='*':
            print("your ans is\n",a*b)
        else:
            print("please choos a velid opreter")
        e=input("\nWrite your expirians about claculater\n")
        print(e)
        print("\n thanx for feed bake")
    again()
def again():
    speak("do you waant reopen this calcluter prees 'y' and close this calcluter prees 'n'")
    c=input("""
    
    do you waant reopen this calcluter 


    prees 'y' and close this calcluter prees 'n'""")
    if c=="y":
        calcy()
        print("thancx for reopen this calculater....")
    elif c=="n":
        print("see you leater.......")
    else:
        print("you not prees any kee..\n")
        print("so i reopen this calculater\n")
        calcy()
calcy()