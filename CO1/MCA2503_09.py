word1=list(input("Enter the first word:"))

first_char=word1[0]
last_char=word1[len(word1)-1]

word1[len(word1)-1]= first_char
word1[0]= last_char

print(word1)



