def pat():
    global colm
    global rowm
    for i in range(len(name)):
        if name[i]=="A":
        # "A" 
            print_A=[[" " for i in range(8)]for j in range(13)]
            for row in range(13):
                for col in range(8):
                    if ((col ==0 or col == 7 )and (row!=0))or ((row==0 or row==6)and (col >0 and col < 7)):
                        print_A[row][col] = "A"
                    else:
                        print(end="  ")
                print()
            list2.append(print_A)
        elif name[i]=="B":
            # "B" 
            print_B=[[" " for i in range(8)]for j in range(13)]
            for row in range(13):
                for col in range(8):
                    if (col ==0)or (col == 7 and (row!=0 and row!=6 and row != 12))or ((row==0 or row==6 or row == 12)and (col>0 and col < 7)):
                        print_B[row][col] = "B"

                    else:
                        print(end="  ")
                print()
            list2.append(print_B)
        elif name[i]=="C":
            # "C"

            print_C=[[" " for i in range(8)]for j in range(13)]
            for row in range(13):
                for col in range(8):
                    if ((col==0)and(row!=0 and row !=12))or ((row==0 or row ==12)and(col>0 and col<7)):
                        print_C[row][col]="C"
                    else:
                        print(end="  ")
                print()
            list2.append(print_C)
        elif name[i]=="D":  
            # "D" 
            print_D=[[" " for i in range(8)]for j in range(13)]
            for row in range(13):
                for col in range(8):
                    if (col==2)or((col == 7 )and(row!=0 and row !=12))or ((row==0 or row ==12)and(col>0 and col<7)):
                        print_D[row][col]="D"
                    else:
                        print(end="  ")
                print()
            list2.append(print_D)
        elif name[i]=="E":
            #"E" 
            print_E=[[" " for i in range(8)]for j in range(13)]

            for row in range(13):
                for col in range(8):
                    if (col==0)or ((row==0 or row ==12 or row == 6)and(col>0 and col<7)):
                        print_E[row][col]="D"
                    else:
                        print(end="  ")
                print()
            list2.append(print_E)
        elif name[i]=="F":
            #"F" 
            print_F=[[" " for i in range(8)]for j in range(13)]

            for row in range(13):
                for col in range(8):
                    if (col==0)or ((row==0 or row == 6)and(col>0 and col<7)):
                        print_F[row][col]="F"
                    else:
                        print(end="  ")
                print()
            list2.append(print_F)
        elif name[i] == "G":
            # "G" 
            print_G=[[" " for i in range(8)]for j in range(13)]

            for row in range(13):
                for col in range(8):
                    if ((col == 0) and (row != 0 and row != 12))or ((col ==7)and (row == 0 or row >5 and row != 12))or((col==6 or col == 5 or col== 4)and (row ==6 )) or ((row == 0 or row == 12)and (col>0 and col <7)):
                        print_G[row][col]="G"
                    else:
                        print(end="  ")
                print()
            list2.append(print_G)
        elif name[i]=="H":
            #"H" 
            print_H=[[" " for i in range(8)]for j in range(13)]

            for row in range(13):
                for col in range(8):
                    if (col == 0 or col == 7)or(col<7 and row ==6) and (col>0 and col <7):
                        print_H[row][col]="H"
                    else:
                        print(end="  ")
                print()
            list2.append(print_H)
        elif name[i]=="I":
            #"I" 
            print_I=[[" " for i in range(8)]for j in range(13)]

            for row in range(13):
                for col in range(8):
                    if col == 3 or row == 0 or row == 12:
                        print_I[row][col]="I"
                    else:
                        print(end="  ")
                print()
            list2.append(print_I)
        elif name[i]=="J":
            #"J" 
            print_J=[[" " for i in range(8)]for j in range(13)]

            for row in range(13):
                for col in range(8):
                    if (col == 6 and row != 12)or (row==0 and col >4) or row == 12 and(col>0 and col<6):
                        # print("J",end=" ")
                        print_J[row][col]="J"
                    else:
                        print(end="  ")
                print()
            list2.append(print_J)
        elif name[i]=="K":
            #"K" 
            print_K=[[" " for i in range(8)]for j in range(13)]

            for row in range(13):
                for col in range(8):
                    if (col == 0)or (row ==6 and col <2)or ((row ==5 or row == 7) and (col ==2)) or ((row ==4 or row == 8) and (col ==3))or ((row ==3 or row == 9) and (col ==4))or ((row ==2 or row == 10) and (col ==5))or ((row ==1 or row == 11) and (col ==6))or ((row ==0 or row == 12) and (col ==7)):
                        print_K[row][col]="K"
                    else:
                        print(end="  ")
                print()
            list2.append(print_K)
        elif name[i]=="L":
            #"L" 
            print_L=[[" " for i in range(8)]for j in range(13)]

            for row in range(13):
                for col in range(8):
                    if col==0 or row == 12:
                        print("L",end=" ")
                        print_L[row][col]="L"
                    else:
                        print(end="  ")
                print()
            list2.append(print_L)
        elif name[i]=="M":
            colm += 2 
            #"M" 
            print_M=[[" " for i in range(10)]for j in range(13)]

            for row in range(13):
                for col in range(10):
                    if (col==0 or col == 9) or ((col==1 or col == 8) and row == 0)or((col==2 or col == 7) and row == 1)or((col==3 or col == 6) and row == 2)or((col == 4 or col == 5) and row == 3):
                        print_M[row][col]="M"
                    else:
                        print(end="  ")
                print()
            list2.append(print_M)
        elif name[i]=="N":
            colm += 2
            rowm -= 5
            #"N" 
            print_N=[[" " for i in range(10)]for j in range(8)]

            for row in range(8):
                for col in range(10):
                    if (col==0 or col == 9) or (col==1 and row == 0)or(col==2 and row == 1)or(col==3 and row == 2)or(col == 4 and row == 3)or(col == 5 and row == 4)or(col == 6 and row == 5)or(col == 7 and row == 6)or(col == 8 and row == 7):
                        print_N[row][col]="N"
                    else:
                        print(end="  ")
                print()
            list2.append(print_N)
        elif name[i]=="O":
            # "O" 
            print_O=[[" " for i in range(8)]for j in range(13)]

            for row in range(13):
                for col in range(8):
                    if ((col==0 or col == 7)and (row != 0 and row != 12)) or (row == 0 or row == 12) and (col >0 and col <7):
                        print_O[row][col]="O"
                    else:
                        print(end="  ")
                print()
            list2.append(print_O)
        elif name[i]=="P":
            # "P" 
            print_P=[[" " for i in range(8)]for j in range(13)]

            for row in range(13):
                for col in range(8):
                    if (col==0 and row != 0)  or (col == 7 and row <7 and row != 0 and row != 6) or (row == 0 or row == 6) and (col >0 and col <7):
                        print_P[row][col]="P"
                    else:
                        print(end="  ")
                print()
            list2.append(print_P)
        # elif name[i]=="Q":
        elif name[i]=="R":
            # "R" 
            print_R=[[" " for i in range(8)]for j in range(13)]

            for row in range(13):
                for col in range(8):
                    if (col==0 and row != 0)  or (col == 7 and row <7 and row != 0 and row != 6) or (col == 1 and row == 7) or (col == 2 and row == 8) or (col == 3 and row == 9) or (col == 4 and row == 10) or (col == 5 and row ==11) or (col == 6 and row == 12)or (row == 0 or row == 6) and (col >0 and col <7):
                        print("R",end=" ")
                        print_R[row][col]="R"
                    else:
                        print(end="  ")
                print()
            list2.append(print_R)
        # elif name[i]=="S":
        # elif name[i]=="T":
        # elif name[i]=="U":
        # elif name[i]=="V":
        # elif name[i]=="W":
        # elif name[i]=="X":
        # elif name[i]=="Y":
        # elif name[i]=="Z":
        else:
            print('INVALID')

        
    return list2
colm = 8
rowm= 13
name = input("Enter Your Name:")
list2=[]
list3=pat()

for i in range(rowm):
    for j in range(len(list3)):
        for k in range(colm):
            print(list3[j][i][k],end=" ")
        print(end=" ")
    print()
