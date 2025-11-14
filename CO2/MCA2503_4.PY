import math
for i in range(1000,9999):
    sqrt=math.sqrt(i)
    if(i%2==0 and sqrt.is_integer()):
        print(i)

        
