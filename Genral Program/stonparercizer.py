def gam():
    import random
    import time
    import squr as S
    
    number_of_try=1


    
    print(" i am your game maneger i help you the ply game and talk you score")
    S.speak(" i am your game maneger ")
    print("game try is limited to only 9 times: ")
    S.speak("game try is limited to only 9 times:")
    print("*THIS IS A STONE,PAPER,CIZER GAME*")
    S.speak("*THIS IS A STONE,PAPER,CIZER GAME*")
    time.sleep(1)
    your_point=0
    computer_point=0
    while (number_of_try<=9):
        print("S for stoan")
        S.speak("S for stoan")
        # time.sleep(1)
        print("P for paper")
        S.speak("P for paper")
        # time.sleep(1)
        print("C for cizer") 
        S.speak("C for cizer")   
        # time.sleep(1)
        S.speak("coose your vote:")
        a=input("coose your vote:")
        print(f"you choose a {a}")
        S.speak(f"you choose a {a}")
        c=["S","P","C"]
        time.sleep(1)
        b=random.choice(c)
        print(f"A computer choose a {b}")
        S.speak(f"A computer choose a {b}")

        #-----------------------------------------------------------------------
        if a=="S" and b=="P":
        
            print("you lose")
            S.speak("you lose")
            computer_point=computer_point+1
            print(f"\ncomputer point is {computer_point}")
            S.speak(f"\ncomputer point is {computer_point}")
        
        elif a=="S" and b=="S":
            print("game is tie")
            S.speak("game is tie")
        elif a=="S" and b=="C":
            your_point=your_point+1
            print("you won")
            S.speak("you won")
            print(f"\nyour point is{your_point}")
            S.speak(f"\nyour point is{your_point}")
        #-----------------------------------------------------------------------
        elif a=="P" and b=="P":
            print("game is tie")
            S.speak("game is tie")
        elif a=="P" and b=="S":
            print("you won")
            S.speak("you won")
            your_point=your_point+1
            print(f"\nyour point is{your_point}")
            S.speak(f"\nyour point is{your_point}")
        elif a=="P" and b=="C":
            print("you lose")
            S.speak("4you lose")
            computer_point=computer_point+1
            print(f"\ncomputer point is{computer_point}")
            S.speak(f"\ncomputer point is{computer_point}")
        #-----------------------------------------------------------------------
        elif a=="C" and b=="C":
            print("game is tie")
            S.speak("game is tie")
        elif a=="C" and b=="S":
            print("you loss")
            S.speak("you loss")
            computer_point=computer_point+1
            print(f"\ncomputer point is{computer_point}")
            S.speak(f"\ncomputer point is{computer_point}")
        elif a=="C" and b=="P":
            print("you won")
            S.speak("you won")
            your_point=your_point+1
            print(f"\nyour point is{your_point}")
            S.speak(f"\nyour point is{your_point}")
        #-----------------------------------------------------------------------
    
        else:
            print("choos a cepital leater")
            S.speak("choos a cepital leater")
            print("please enter a singal leater")
            S.speak("please enter a singal leater")
        
    

     
        print(number_of_try,"no.of try he took to finish\n")
        

    

        print(9-number_of_try,"no. of try left\n\n")
    
        number_of_try = number_of_try + 1
    if(number_of_try>9):

        print("Game Over")
        S.speak("Game Over")


    if your_point<computer_point:
        print(f"you lose the game becauae your point is {your_point} and computer point is {computer_point}\n")
        S.speak(f"you lose the game becauae your point is {your_point} and computer point is {computer_point}\n")
    elif your_point>computer_point:
        print(f"you won the game becauae your point is {your_point} and computer point is {computer_point}\n")
        S.speak(f"you won the game becauae your point is {your_point} and computer point is {computer_point}\n")

        
    again()

def again():
    cal_again = input('''

    Do you want to play game again?

    Please type y for YES or n for NO.

    ''')



    if cal_again == 'y':
        print("YOU RETURN OPEN THIS GAME ")

        gam()

    elif cal_again == 'n':

        print("See You Later")

    else:

        gam()
if __name__ == "__main__":
    
    gam()
