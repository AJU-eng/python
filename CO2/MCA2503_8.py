import math
words=['mouse','keyboard','monitor','cpu','ups']

lengths=[]

for i in words:
    lengths.append(len(i))

print(max(lengths))
