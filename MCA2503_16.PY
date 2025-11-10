string1=list(input("enter the first word:"))
string2=list(input("enter the second word:"))


charA=string1[1]
charB=string2[1]

string1[1]=charB
string2[1]=charA

stringa="".join(string1)
stringb="".join(string2)

print(stringa+stringb )
