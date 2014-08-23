import random
import math
import copy
def udaljenost(a,b):
    ud=0
    for i in range(d):
        ud=ud+(a[i]-b[i])*(a[i]-b[i])
    return ud
        
def fja_cilja(centri,tocke,cid):
    suma=0
    for i in range(n):
        suma=suma+udaljenost(tocke[i],centri[cid[i]])
    return suma

f=open("podaci4.txt","r")

k=int(f.readline()) #broj centara
n=int(f.readline()) #broj tocaka
d=int(f.readline()) #dimenzija prostora

tocke=[]
for i in range(n):
    line=f.readline()
    vector=line.split()
    tocke.append(vector)

f.close()

for i in range(n):
    for j in range(d):
        tocke[i][j]=float(tocke[i][j])

centri1=[]
for i in range(k): # biramo potrebni broj slucajnih centara
        j=random.randint(0, n-1)
        centri1.append(tocke[j][:])

centri2=[]
pom=[]

for i in range(d):
    pom.append(0)

for i in range(k):
    centri2.append(pom[:])

cid1=[]
for i in range(n):
    utc=[]
    for j in range(k):
        utc.append(udaljenost(tocke[i][:],centri1[j][:]))
    cid1.append(utc.index(min(utc[:])))                

for pon in range(6):
    vs=[]
    pom=[]
    for i in range(d):
        pom.append(0)
    count=[]
    for i in range(k):
        vs.append(pom[:])
        count.append(0)
        for j in range(n):
            if cid1[j]==i:
                count[i]=count[i]+1
                for l in range(d):
                    vs[i][l]=vs[i][l]+tocke[j][l]
    print "cid1", cid1
    for i in range(k):
        for j in range(d):
            if count[i]!=0:
                centri1[i][j]=vs[i][j]/count[i]
    cid1=[]
    for i in range(n):
        utc=[]
        for j in range(k):
            utc.append(udaljenost(tocke[i][:],centri1[j][:]))
        cid1.append(utc.index(min(utc[:])))
    srediste=[]
    for j in range(d):
        suma=0
        for i in range(k):
            suma=suma+centri1[i][j]
        srediste.append(suma/k)    
    for i in range(k):
        for j in range(d):
            centri2[i][j]=2*srediste[j]-centri1[i][j]
    cid2=[]
    for i in range(n):
        utc=[]
        for j in range(k):
            utc.append(udaljenost(tocke[i][:],centri2[j][:]))
        cid2.append(utc.index(min(utc[:])))
    f1=fja_cilja(centri1[:],tocke[:],cid1[:])
    f2=fja_cilja(centri2[:],tocke[:],cid2[:])
    alfa=math.exp((f1-f2)*((pon*pon)/100000000000000))
    beta=random.random()
    print "cid1", cid1
    print "centri1", centri1
    print "cid2", cid2
    print "centri2", centri2
    if f1>f2:
        centri1=copy.deepcopy(centri2)
        cid1=copy.deepcopy(cid2)
        print "zamijenio sam ih jer je f1 veci", cid1
    else:
        if beta<alfa:
            centri1=copy.deepcopy(centri2)
            cid1=copy.deepcopy(cid2)
            print "mijenjam ih jer je toplo", cid1
    print "Prva_fja...", f1
    print "Druga_fja...", f2
