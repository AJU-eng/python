word=list(input("Enter the word:"))
dic={}
for i in range(0,len(word)):
    char=word[i]
    count=0
    for j in range(0,len(word)):
        if(char==word[j]):
            count=count+1
    dic.update({char:count})

print(dic)
