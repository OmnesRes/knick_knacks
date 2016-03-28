f=open('parsed.txt')

mrnas={}
sequence={}
rawdata=[]
for i in f:
    rawdata.append([j.strip() for j in i.split("\t")[:-1]])



for i in rawdata:
    if mrnas.has_key(i[0])==False:
        mrnas[i[0]]=[i[1:5]]
        mrnas[i[0]].append([i[5:-1]])
        sequence[i[6]]=i[-1]
    else:
        mrnas[i[0]][1].append(i[5:-1])
        sequence[i[6]]=i[-1]

    
