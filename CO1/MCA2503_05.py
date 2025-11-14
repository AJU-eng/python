integers=[1,2,3,100,6,7,8,200]

for i in range(0,len(integers)):
    if(integers[i]>=100):
        integers[i]="over"

print(integers)
