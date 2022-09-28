
def Matrix(m,n):
    o=[]
    for i in range(m):
        row=[]
        for j in range(n):
            inp=int(input(f"Enter O[{i}][{j}]"))
            row.append(inp)
        o.append(row)
    return o

def sum(a,b):
    output=[]
    for i in range(len(a)): # Number of rows
        row=[]
        for j in range(len(b)):# Number of colums
            row.append(a[i][j]+b[i][j])
        output.append(row)
    return output
            
m=int(input('enter the value m\n'))
n=int(input('enter the value n\n'))

print("Enter Matrix A")

A=Matrix(m,n)

print("Enter Matrix b")

B=Matrix(m,n)

print(A)
print(B)


print("=")
sum=sum(A,B)
print(sum)
