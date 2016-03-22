from Bio.Seq import Seq
import re
execfile('dictionaries.py')


accession={}
for i in mrnas:
    for j in mrnas[i][1]:
        try:
            accession[j[1]]=[int(j[-2])-1,int(j[-1])]
        except:
            pass

def mut(position,transcript,mutation):
    protein=Seq(sequence[transcript][accession[transcript][0]:accession[transcript][1]]).translate()
    if position-9<0:
        return protein[0:position-1]+mutation+protein[position:position+8]
    else:
        return protein[position-9:position-1]+mutation+protein[position:position+8]


f=open(r'firebrowser_GBM_20150410\MANIFEST.txt')
maf_patients=[]
maf_files=[]
for i in f:
    maf_patients.append(i.split()[1].split('.')[0][:-3])
    maf_files.append(i.split()[1])


peptides={}
for i,j in zip(maf_patients,maf_files):
    f=open(r"firebrowser_GBM_20150410"+'\\'+j)
    f.readline()
    for k in f:
        data=k.split('\t')
        if data[8]=='Missense_Mutation':
            try:
                peptides[i]=peptides.get(i,[])+[str(mut(int(re.findall('[0-9]+',data[41])[0]),data[43],re.split('[0-9]+',data[41])[-1]))]
            except:
                pass



nonamer_peptides={}
for i in peptides:
    for j in peptides[i]:
        if '*' in j:
            j=j[0:j.find('*')]
        for k,l in zip(range(0,len(j)-8),range(9,len(j)+1)):
            if len(j[k:l])==9:
                nonamer_peptides[i]=nonamer_peptides.get(i,[])+[j[k:l]]
            
            
tetra_peptides={}

for i in nonamer_peptides:
    for j in nonamer_peptides[i]:
        for k,l in zip(range(0,len(j)-3),range(4,len(j)+1)):
            if len(j[k:l])==4:
                tetra_peptides[i]=tetra_peptides.get(i,[])+[j[k:l]]



nonamer_counts={}
for i in nonamer_peptides:
    for j in nonamer_peptides[i]:
        nonamer_counts[j]=nonamer_counts.get(j,0)+1



tetra_counts={}
for i in tetra_peptides:
    for j in tetra_peptides[i]:
        tetra_counts[j]=tetra_counts.get(j,0)+1

















