number=int(input("Enter the number:"))
factors=[]
for i in range (1,number):
    if(number%i==0):
        factors.append(i)

print(factors)
