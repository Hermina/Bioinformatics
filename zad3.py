import math
f=open("emisijske.txt","r")

em=[]
for i in range(2):
    line=f.readline()
    vector=line.split()
    em.append(vector)

f.close()

f=open("tranzicijske.txt","r")

tran=[]
for i in range(2):
    line=f.readline()
    vector=line.split()
    tran.append(vector)

f.close()

for i in range(2):
    for j in range(2):
        tran[i][j]=float(tran[i][j])

for i in range(2):
    for j in range(6):
        em[i][j]=float(em[i][j])

niz="1234661234666661234"
ln=len(niz)
x=[]
for i in range(ln):
    x.append(0)
    x[i]=int(niz[i])
f=[]
pom=[]
for i in range(ln):
    pom.append(0)
for i in range(2):
    f.append(pom[:])

f[0][0]=0.5*em[0][x[0]-1]
f[1][0]=0.5*em[1][x[0]-1]
for i in range(ln-1):
    f[0][i+1]=(f[0][i]*tran[0][0]+f[1][i]*tran[1][0])*em[0][x[i+1]-1]
    f[1][i+1]=(f[0][i]*tran[0][1]+f[1][i]*tran[1][1])*em[1][x[i+1]-1]

rjf=f[0][ln-1]+f[1][ln-1]

g=[]
for i in range(2):
    g.append(pom[:])

g[0][ln-1]=1
g[1][ln-1]=1

for i in range(ln-1):
    g[0][ln-i-2]=g[0][ln-i-1]*tran[0][0]*em[0][x[ln-i-1]-1]+g[1][ln-1-i]*tran[0][1]*em[1][x[ln-i-1]-1]
    g[1][ln-i-2]=g[0][ln-i-1]*tran[1][0]*em[0][x[ln-i-1]-1]+g[1][ln-1-i]*tran[1][1]*em[1][x[ln-i-1]-1]

rjb=g[0][0]*em[0][x[0]-1]+g[1][0]*em[1][x[0]-1]

probaup=g[0][14]*f[0][14]/rjf
probaun=g[1][14]*f[1][14]/rjf
print probaup
print probaun
