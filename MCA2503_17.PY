dict1={"a":10,"b":30,"c":20}

for key in sorted(dict1,key=dict1.get):
    print(key,":",dict1[key])
