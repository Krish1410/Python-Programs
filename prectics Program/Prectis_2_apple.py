apple=int(input("Enter the amount of APPLE:"))
mn=int(input("Enter The minimam Value:"))
mx=int(input("Enter The maximam Value:"))

for i in range(mn,mx+1):
    if apple%i==0:
        print(f"{i} is dvided by {apple}")
