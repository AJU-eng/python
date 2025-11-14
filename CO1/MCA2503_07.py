list1=[1,2,3,4,5]
list2=[4,5,6,7,8]

sum1=0
sum2=0

for i in list1:
    sum1=sum1+i

for i in list2:
    sum2=sum2+i

len1=len(list1)
len2=len(list2)

common=set(list1)& set(list2)



print("List are of same length:","yes" if len1==len2 else "no")
print("List sum to same value:","yes" if sum1==sum2 else "no")
print("Any common value occur in both:","yes" if common else "no")



