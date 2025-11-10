num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))

if num1<num2:
    if(num2<num3):
        print("3rd Number is greatest")
    else:
        print("2nd Number is greatest")
    
else:
    print("1st Number is greatest")

