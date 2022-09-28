def next_palidrom(n):
    n=n+1
    while not is_palidrom(n):
        n+=1
    return n
def is_palidrom(n):
    return str(n)==str(n)[::-1]
if __name__ == "__main__":
    # ___________________________Taking the in put form users________________________
    size=int(input("Hoe Many Values you enter:"))
    palidrom_list=[]
    for i in range(size):
        palidrom_list.append(int(input(f"Enter The {i} Value:")))
    # ___________________________Finish Taking the in put form users_________________
    new_palidrom=[]
    for element  in palidrom_list:
        if element>=10:
            n=next_palidrom(element)
            new_palidrom.append(n)
        else:
            new_palidrom.append(element)
    for i in range(size):
            print(f"The next palodrom of {palidrom_list[i]} is {new_palidrom[i]}")
