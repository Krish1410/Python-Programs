with open('K:/python/curancy.txt') as f:
    lines = f.readlines()

curancydict={}
for line in lines:
    par=line.split("\t")
    curancydict[par[0]]=par[1]
amout=int(input("Enter the currence:\n"))
print("Choos a reagion to cunvert you currancy")
[print(curancy) for curancy in curancydict]
reagion=input("Enter a reagion name")
print(f"{amout} INR is {amout*float(curancydict[par[0]])} in {reagion}")