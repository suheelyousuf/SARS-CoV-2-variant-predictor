import pandas as pd
import numpy as np
import os
import csv


from Bio import SeqIO

cols = ['sequence', 'lineage']
row=[]


#result = pd.read_csv('../data/lineage_alpha.csv',skiprows=[0])
#print(result)
flag=True
with open("../data/Alpha/gisaid_hcov-19_2022_11_30_11- Alpha.fasta") as handle1, open('../data/lineage_alpha.csv') as handle2:
    for record,linage in zip(SeqIO.parse(handle1, "fasta"),csv.reader(handle2, delimiter=',')):
        if flag==True:
            flag=False
            continue
        #print(linage)
        row.append([str(record.seq),linage[1]])
        


df = pd.DataFrame(row, columns=cols)

#print(df)

row=[]

flag=True
with open("../data/Beta/gisaid_hcov-19_2022_11_30_12- Beta.fasta") as handle1, open('../data/lineage_beta.csv') as handle2:
    for record,linage in zip(SeqIO.parse(handle1, "fasta"),csv.reader(handle2, delimiter=',')):
        if flag==True:
            flag=False
            continue
        #print(linage)
        row.append([str(record.seq),linage[1]])
        


df1 = pd.DataFrame(row, columns=cols)
df=df.append(df1,ignore_index=True)

row=[]

flag=True
with open("../data/Gamma/gisaid_hcov-19_Gamma2022_11_30_11.fasta") as handle1, open('../data/lineage_gamma.csv') as handle2:
    for record,linage in zip(SeqIO.parse(handle1, "fasta"),csv.reader(handle2, delimiter=',')):
        if flag==True:
            flag=False
            continue
        #print(linage)
        row.append([str(record.seq),linage[1]])
        


df1 = pd.DataFrame(row, columns=cols)
df=df.append(df1,ignore_index=True)


row=[]

flag=True
with open("../data/Delta/gisaid_hcov-19_Delta 2022_11_30_11.fasta") as handle1, open('../data/lineage_delta.csv') as handle2:
    for record,linage in zip(SeqIO.parse(handle1, "fasta"),csv.reader(handle2, delimiter=',')):
        if flag==True:
            flag=False
            continue
        #print(linage)
        row.append([str(record.seq),linage[1]])
        


df1 = pd.DataFrame(row, columns=cols)
df=df.append(df1,ignore_index=True)


row=[]

flag=True
with open("../data/Omicron/gisaid_hcov-19_Omicron 2022_11_30_11.fasta") as handle1, open('../data/lineage_omicron.csv') as handle2:
    for record,linage in zip(SeqIO.parse(handle1, "fasta"),csv.reader(handle2, delimiter=',')):
        if flag==True:
            flag=False
            continue
        #print(linage)
        row.append([str(record.seq),linage[1]])
        


df1 = pd.DataFrame(row, columns=cols)
df=df.append(df1,ignore_index=True)


#print(df)

df=df.sample(frac=1)

f=open('../data/linage_random_samples_all.txt','w')

df.to_csv(f, sep='\t',index=False)



