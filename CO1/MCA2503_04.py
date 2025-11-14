sentence="my name is Ajay and my passion is Technology"

list_sentence=sentence.split()



for i in list_sentence:
    word=i
    count=0
    for j in list_sentence:
        if(word==j):
            count=count+1
    print(i,count)
