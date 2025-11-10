filename=input("Enter the file name(with extension):")
split=list(filename)
print(split)

for i in range(0,len(split)):
    if(split[i]=='.'):
        extracted=split[i+1:]
        print(''.join(extracted))
        break;
    
