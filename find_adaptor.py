f=open('fastq file')

##parse fastq file

reads=[]
x=f.readline()
while x!='':
    reads.append(f.readline().strip())
    f.readline()
    f.readline()
    x=f.readline()

##find k_mers

k_mers={}

for read in reads[:100000]:
    for pos in range(6,30):
        k_mers[read[:pos]]=k_mers.get(read[:pos],0)+1

##convert dictionary to list and sort

mylist=zip(k_mers.values(),k_mers.keys())

mylist.sort(reverse=True)


##print most abundant k_mers

for i in mylist[:50]:
    print i
