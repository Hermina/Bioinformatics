import random
import math
import copy
def udaljenost(a,b):
    ud=0
    for i in range(d):
        ud=ud+(a[i]-b[i])*(a[i]-b[i])
    return ud

def fja_cilja(cen,tocke,ci):
    suma=0
    for i in range(n):
        suma=suma+udaljenost(tocke[i],cen[ci[i]])
    return suma

def samaraj(centri):
    srediste=[]
    centri2=[]
    pom=[];
    for i in range(d):
        pom.append(0)
    for i in range(k):
        centri2.append(pom[:])
    for j in range(d):
        suma=0
        for i in range(k):
            suma=suma+centri[i][j]
        srediste.append(suma/k)
    x=random.random()
    x=2*x-0.8
    print "samaram", x
    for i in range(k):
        for j in range(d):
            centri2[i][j]=x*(-srediste[j]+centri[i][j])+centri[i][j]
    return centri2

def samaraj2(centri):
    srediste=[]
    centri2=[]
    pom=[];
    for i in range(d):
        pom.append(0)
    for i in range(k):
        centri2.append(pom[:])
    for j in range(d):
        suma=0
        for i in range(k):
            suma=suma+centri[i][j]
        srediste.append(suma/k)
    print " "
    for i in range(k):
        x=random.random()
        x=x-0.5
        for j in range(d):
            centri2[i][j]=x*(-srediste[j]+centri[i][j])+centri[i][j]
    return centri2
    
f=open("podaci25.txt","r")

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
        
centri=[]
for i in range(k): # biramo potrebni broj slucajnih centara
        j=random.randint(0, n-1)
        centri.append(tocke[j][:])
cid=[]
for i in range(n):
    utc=[]
    for j in range(k):
        utc.append(udaljenost(tocke[i][:],centri[j][:]))
    cid.append(utc.index(min(utc[:])))                
vs=[]
pom=[]

#racunamo nove centre
for i in range(d):
    pom.append(0)
count=[]
for i in range(k):
    vs.append(pom[:])
    count.append(0)
    for j in range(n):
        if cid[j]==i:
            count[i]=count[i]+1
            for l in range(d):
                vs[i][l]=vs[i][l]+tocke[j][l]
for i in range(k):
    for j in range(d):
       if (count[i]!=0): centri[i][j]=vs[i][j]/count[i]
cid=[]

#nova podjela tocaka u klastere
for i in range(n):
    utc=[]
    for j in range(k):
        utc.append(udaljenost(tocke[i][:],centri[j][:]))
    cid.append(utc.index(min(utc[:])))
minimum=100000
#KRECE ALGORITAM
for pon in range(500):
    
    #samaramo i racunamo njihove klastere
    if (pon%10==0):
        centri2=samaraj2(centri[:][:]);
    else:
        centri2=samaraj(centri[:][:]);
    cid2=[]
    for i in range(n):
        utc=[]
        for j in range(k):
            utc.append(udaljenost(tocke[i][:],centri2[j][:]))
        cid2.append(utc.index(min(utc[:])))
    vs=[]
    pom=[]
    #racunamo nove centre
    for i in range(d):
        pom.append(0)
    count=[]
    for i in range(k):
        vs.append(pom[:])
        count.append(0)
        for j in range(n):
            if cid2[j]==i:
                count[i]=count[i]+1
                for l in range(d):
                    vs[i][l]=vs[i][l]+tocke[j][l]
    for i in range(k):
        for j in range(d):
           if (count[i]!=0): centri2[i][j]=vs[i][j]/count[i]
    cid2=[]
    #nova podjela tocaka u klastere
    for i in range(n):
        utc=[]
        for j in range(k):
            utc.append(udaljenost(tocke[i][:],centri2[j][:]))
        cid2.append(utc.index(min(utc[:])))

    f1=fja_cilja(centri[:],tocke[:],cid[:])
    f2=fja_cilja(centri2[:],tocke[:],cid2[:])
    alfa=math.exp((f1-f2)*(pon)/600000000)
    
    #print "Broj iteracije...", pon
    print "Vrijednost 1.funkcije cilja...", f1
    print "Vrijednost 2.funkcije cilja...", f2
    #print "Trenutni 1.centri...", centri
    #print "Trenutni 2.centri...", centri2
    print "alfa", alfa
    beta=random.random()
    if f1<minimum:
        minimum=copy.deepcopy(f1)
    if f1>f2:
        centri=copy.deepcopy(centri2)
        cid=copy.deepcopy(cid2)
    else :
        if beta<alfa:
            centri=copy.deepcopy(centri2)
            cid=copy.deepcopy(cid2)
    polje=[]
    for l in range (25):
        polje.append(0);
    for l in range (10000):
        polje[cid[l]]=polje[cid[l]]+1;
    print "count", polje    

#print "klasteri", cid
