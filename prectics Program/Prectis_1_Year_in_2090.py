def Year_In_100():
    print("Enter your age or birth of year: ")
    Year_or_age=int(input())
    currant_year=2020
    age=False
    Year=False

    if Year_or_age>1900:
        if Year_or_age > 2020:
            print("You Are not born")
        else:
            currant_age=(currant_year-Year_or_age)
            Year_in_100=currant_year+(100-currant_age)
            print(f"Your Age is {currant_age}")
            Year=True
            if Year_in_100 < 2020:
                print(f"You Are alredy 100 Year old in {Year_in_100}")
            else:
                print(f"In {Year_in_100} you age is 100")
    elif Year_or_age>0 or Year_or_age <= 0:
        if Year_or_age>100:
            print("you Are alredy 100 or abou")
        else:
            if Year_or_age<=0:
                print("You Are not Born")
            else:
                if Year_or_age > 200:
                    print("Sorry! You Are Ded or You Enter a Wrong Age ")
                else:
                    Year_in_100=currant_year+(100-Year_or_age)
                    age=True
                    print(f"In {Year_in_100} Your Aag is 100")
    print("Can you know what is your age in other year {y/n}: ")
    Know=input()
    if age==True and Know=='y':
        Year=int(input("Enter the year: "))
        if Year < currant_year:
            age=Year-currant_year
        else:
            age=abs(Year-currant_year)
        now_age=(age)+Year_or_age
        if now_age <=0:
            print("You Are not Born At this time OK!")
        else:
            print(f"You age in {Year} is {now_age}")
    elif Year==True and Know=='y':

        Year=int(input("Enter the year: "))
        if Year > Year_or_age:
            age=abs(Year-Year_or_age)
            currant_age=currant_year-Year_or_age
            now_age=age+currant_age
        else:
            print("you are not yet born")
        print(f"You age in {Year} is {now_age}")


if __name__ == "__main__":
    Year_In_100()
    while(True):
        continu=input("You Rechek or Restat The App(y/n): ")
        if continu=='y':
            Year_In_100()
        elif continu == 'n':
            exit()
        else:
            print("Enter a Write Input")
            continue
