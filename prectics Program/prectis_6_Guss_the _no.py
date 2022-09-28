# This Is Tow Player game
import random

def GameLoop(Real_Number):
    '''
    This is Main Funcshion of "Guss the number" game.
    This Funshion Take only 1 Argument:
    "Real_Number=This a number Who Guss by Players "
    '''
    # 1.Take a Input and create a tryes variable
    Guss=int(input("Enter your Chois:"))
    Tryes=1
    # 2.This is loop for take a input and give a hint to player

    while Guss != Real_Number:
        if Guss>Real_Number:   
            Guss=int(input("\nPlease Enter a Small Value:"))
            Tryes+=1
        else:   
            Guss=int(input("\nPlease Enter a Big Value:"))
            Tryes+=1
    return Tryes
if __name__ == "__main__":
    # 1.Genret a Random number 
    a=int(input("Enter a First Number:"))
    b=int(input("Enter a Second Number:"))
        # A.This Randome for First Player
    Real1=random.randint(a,b)
        # B.This Randome for Second Player
    Real2=random.randint(a,b)
    # 2.Take a Name of Players
    print("")
    Players1_Name=input("Enter your name:")
    Players2_Name=input("Enyer your Friend Name:")

    print(f"Guss The Number Beetwin {a} and {b}")

    # 3.Call The GameLoop Funcshion For 2 Difrent Players
    print(f"{Players1_Name} Turn:\n")
    p1=GameLoop(Real1)
    print(f"{Players2_Name} Turn:\n")
    p2=GameLoop(Real2)
    
    # 4.Dicler a Winner By His/Her Score
    if p1<p2:
        print(f"\nWinner is {Players1_Name}:With His/Her Score {p1}")
        print(f"Sorry! {Players2_Name}:Your Score is {p2}\n")
    elif p2<p1:
        print(f"\nWinner is {Players2_Name}:With His/Her Score {p2}")
        print(f"Sorry! {Players1_Name}:Your Score is {p1}\n")
    else:
        print(f"\nHey! {Players1_Name} and {Players2_Name} Game is TIE!!!\n")

    # 5.Dicler a Real Number
    print(f"{Players1_Name}:\nYour Real Number is {Real1}\n")
    print(f"{Players2_Name}:\nYour Real Number is {Real2}\n")
