f=open('sequence.gb')
rawdata=[]
x=f.readline()
while x!='':
    if "LOCUS" in x[:5]:
        length=x.split()[2]
        x=f.readline()
        rawdefinition=x.strip().split('DEFINITION')[1]
        x=f.readline()
        while 'ACCESSION' not in x:
            rawdefinition+=' '+x.strip()
            x=f.readline()
        accession=x.strip().split()[1]
        x=f.readline()
        X=False
        gene=''
        synonyms=''
        location=''
        entrez_id=''
        while X==False:
            if gene=='':
                if '/gene=' in x:
                    gene=x.strip().split('/gene=')[1].strip('"')
            if entrez_id=='':
                if r'/db_xref="GeneID:' in x:
                    entrez_id=x.strip().split(":")[-1][:-1]
            if synonyms=='':
                if "/gene_synonym=" in x:
                    y=x.split("/gene_synonym=")[1]
                    while True:
                        if '"\n' in x:
                            synonyms+=y.strip()
                            break
                        synonyms+=y.strip()
                        x=f.readline()
                        y=x
            if location=='':
                if "/map=" in x:
                    location=x.split("/map=")[1].strip()
            if "  CDS  " in x:
                if "join" in x:
                    start=x.split("join(")[1].split("..")[0]
                    end=x.split("join(")[1].split("..")[2].strip().split(")")[0]
                else:
                    start=x.split()[1].split("..")[0]
                    end=x.split()[1].split("..")[1].strip()
            if x=='ORIGIN      \n':
                sequence=""
                x=f.readline()
                while x!="//\n":
                    for i in x.strip().split()[1:]:
                        sequence+=i
                    x=f.readline()
                X=True
                genename=rawdefinition.split('('+gene+')')[0].strip()
                transcript=rawdefinition.split('('+gene+'),')[1]
                rawdata.append([gene,genename,entrez_id,location,synonyms,transcript,accession,length,start,end,sequence])
            x=f.readline()
    x=f.readline()

            
f=open('parsed.txt','w')
for i in rawdata:
    for j in i:
        f.write(j)
        f.write("\t")
    f.write("\n")
f.close()


        
        
    
