list_fnames=['Ajay',"Anurag","Rabah","sandul","Adithyan"]

for i in list_fnames:
    count=0
    name=list(i)
    for j in name:
        if(j=="a" or j=="A"):
            count=count+1
    print(i,count)
    
