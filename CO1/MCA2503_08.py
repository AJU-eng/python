word=list(input("Enter the word:"))
first_char=word[0]

for i in range(1,len(word)):
    if(word[i]==first_char):
        word[i]="$"

print("".join(word))
