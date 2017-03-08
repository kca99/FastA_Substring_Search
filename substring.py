import re #finditeration function
import sys #sys.exit function 
Src_name = input('Enter the name of source FASTA file: ')
 
seq=[]
try:
    with open(Src_name) as Src_obj:
        lines = Src_obj.read().replace('>','').splitlines() #removes > from source
        print ('Sequence Name: ', lines[0])
       
        seq_l= lines[2:]
        seq=''.join(seq_l)
    ##    print(seq)
        print('Source Sequence Loaded \n')
        seqstr=str(seq)
except FileNotFoundError:
    print('File not found..Exiting..')
    sys.exit()

Sub_name = input('Enter the name of substring FASTA file: ')
try:
    with open(Sub_name) as Sub_obj:
        subseq= Sub_obj.read()
        #print('Subsequence to search: ', subseq)
        #len=len(subseq)-1 #-1 for /n char
except FileNotFoundError:
    print('File not found..Exiting..')
    sys.exit()
substr=str(subseq)

##print(substr, '\n')
##print(seqstr)
##test=['TCGCGTGGTGGGATCG']
##tests=str(test1[0])
##index= tests.index(substr)
##if seqstr.find(substr)==1:
seqhit=1

try:
    index = seqstr.index(substr)
    
except ValueError:
    print('Error, Substring not found')
    sys.exit()
##print('Subquery found after index: ',index)

for m in re.finditer(substr, seqstr):
        print (' Hit %d index found after ' %(seqhit), m.start())
        seqhit=seqhit+1


