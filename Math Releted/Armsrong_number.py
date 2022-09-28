i=1
for n in range(0,10):
    # No=int(input("Enter the number"))
    No=n
    Sum=0
    Order=len(str(No))
    Copy_No=No
    while(No>0):
        digit=No%10
        Sum += digit **Order
        No=No//10

    if Sum==Copy_No:
        print(f"{Copy_No} is an armsrong number")


