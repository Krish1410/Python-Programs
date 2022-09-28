Count=int(input("How many Friend:"))
names=[]
for i in range(Count):
    Name=input("Enter Name(SurName+Name):")
    names.append(Name.split(" "))
Index=0
while Index!=Count:
    if Index<(Count-1):
        print(names[Index+1][0]+" "+names[Index][1])
    else:
        print(names[0][0]+" "+names[Index][1])

    print(str(Index+1))
    Index+=1


