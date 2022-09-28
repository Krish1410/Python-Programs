def next_palidrom(n):
    n=n+1
    while not is_palidrom(n):
        n+=1
    return n
def is_palidrom(n):
    return str(n)==str(n)[::-1]
if __name__ == "__main__":
    no=int(input("Hoe many valurs you enter:"))
    for i in range(no):
        Value=int(input("Enter The Value:"))
        nextpalidrom=next_palidrom(Value)
        print(f"TRhe next Palidrom of {Value} is {nextpalidrom}")


