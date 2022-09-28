list_=[]
count=int(input("How many Values you enter in list:"))
no=0
while no!=count:
    list_.append(int(input("Enter the lists value:")))
    no+=1
rev1=list_[:]
rev1.reverse()
print(f"Your Reverse list of {list_} is {rev1}")
rev2=list_[::-1]
print(f"You Reverse list if {list_} is {rev2}")
rev3=list_
for i in range(len(list_)//2):
    rev3[i],rev3[len(list_) -i -1]=rev3[len(list_) -i -1],rev3[i]
print(f"You Reverse list if {list_} is {rev3}")