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