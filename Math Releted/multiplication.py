n=int(input("Enter number:"))
Table_Size=11
Qushion=input("You Need a Advance Table like(10x999):")
if Qushion=="Yes" or Qushion=="yes" or Qushion=="Y" or Qushion=="y":
    Table_Size=int(input("How many range you got a table:"))

for i in range(1,Table_Size):
    print(f"{n} x {i} = {n*i}")
