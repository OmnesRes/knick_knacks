import httplib
import base64
from xml.dom import minidom


###load protein sequences
f=open('fasta_uniprot.txt')
x=f.readline().strip()
uniprot={}
while x!='':
    seq=''
    if '>' in x:
        name=x.strip().strip('>')
        x=f.readline()
        while '>' not in x and x!='':
            seq+=x.strip()
            x=f.readline()
        uniprot[name]=seq

all_data=[]
for i in uniprot:
    finaldata={}
    modifications=[]
    unique={}
    class Example1():
        def __init__(self, username, password):
            self.default_headers = { "Authorization" : "Basic %s" % base64.encodestring( "%s:%s" % ( username, password) ).rstrip('\n') }
            self.port = 443
            self.host = 'www.proteomicsdb.org'
            self.testurl = "https://www.proteomicsdb.org/proteomicsdb/logic/api/peptidesperprotein.xsodata/InputParams(PROTEINFILTER='"+i+"')/Results?$select=SEQUENCE,VARIABLE_MODIFICATION_STRING,FIXED_MODIFICATION_STRING&$format=xml"
        
        def connectAndRetrieve(self):
            global body
            hconn = httplib.HTTPSConnection( "%s:%d" % (self.host,self.port) )
            hconn.request("GET", self.testurl, headers = self.default_headers)
            resp = hconn.getresponse()
            print resp.status, resp.reason
            body = resp.read()

        
    ex1=Example1('name','password')
    ex1.connectAndRetrieve()

    x=minidom.parseString(body)
    data=x.getElementsByTagName('m:properties')
    for j in data:
        try:
            if 'Phospho' in j.childNodes[1].childNodes[0].nodeValue:
                modifications.append([j.childNodes[0].childNodes[0].nodeValue,j.childNodes[1].childNodes[0].nodeValue])
        except:
            pass
    for peptide in modifications:
        sequence=peptide[0]
        pep_modifications=[k.strip() for k in peptide[1].split(';')]
        for mod in pep_modifications:
            if 'Phospho' in mod:
                finaldata[str(sequence)+'_'+str(mod.split('@')[1])]=''

    for pep_mod in finaldata:
        sequence=pep_mod.split('_')[0]
        mod_position=int(pep_mod.split('_')[1][1:])
        protein_position=uniprot[i].find(sequence)
        final_position=mod_position+protein_position
        name='Phospho'+'_'+pep_mod.split('_')[1][0]+str(final_position)
        if name not in unique:
            all_data.append([i,name])
            unique[name]=''

f=open('all_modifications.txt','w')
for i in all_data:
    f.write(i[0])
    f.write('\t')
    f.write(i[1])
    f.write('\n')
f.close()
    





