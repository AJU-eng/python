n=int(input("Enter the limit of number pyramid:"))


for i in range(1,n):
    for j in range(1,i+1):  
             print(j*i ,end="")
    print()
