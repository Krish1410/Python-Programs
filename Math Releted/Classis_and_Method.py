'''VariaBales And Lists'''
Class_no=int(input("How many class:"))
Inform_No=int(input("How many Informashion:"))
Class=[]
Center_Price=[]
InforMashion=[]
Value=0
'''Variabal is Finish'''

# 1.Take a class in input
for i in range(Class_no):
    Classes=input("Enter Class(Number - Number):")
    Class.append(Classes.split("-"))
# 2.Get a informashion based on Class
for i in range(Inform_No):
    Informashion=input("Enter [fi]:")
    Informashion=int(Informashion)
    InforMashion.append(Informashion)
# 3.Find a Center prise of class
for First,Last in Class:
    First=int(First)
    Last=int(Last)
    Center_Price.append((First+Last)/2)
    for info in InforMashion:
        if info>= First and info < Last:
            Value+=1
            print(f"{Value} beetwin {First}-{Last}")
            if Last>=First:
                Value=0
                Value=+1
                print(f"{Value} beetwin {First}-{Last}")