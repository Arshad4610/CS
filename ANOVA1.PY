import numpy as np
import pandas as pd
import scipy.stats as ss
n=int(input("Enter no.of treatements:"))
nt=input("Enter names of treatments:")
tr=[]
for i in range(n):
    x=[float(x) for x in input().split(',')]
    tr.append(x)
ti=0
p=0
rss=0
N=0
for i in tr:
    ti+=sum(i)
    p+=sum(i)**2/len(i)
    rss+=sum(np.square(i))
    N+=len(i)
print(ti)
print(p)
CF=ti**2/N
print("RSS :",rss)
print("CF :",CF)
alpha=float(input("Enter l.o.s:"))
SST=round((rss-CF),3)
print("SST:",SST)
SStr=round((p-CF),3)
print("SStr :",SStr)
SSe=round((SST-SStr),3)
print("SSe:",SSe)
Msstr=round((SStr/(n-1)),3)
Msse=round((SSe/(N-n)),3)
Fcal=round((Msstr/Msse),3)
print("Fcal:",Fcal)
ANOVA={
    "Sov":[nt,"error","total"],
    "Sos":[SStr,SSe,SST],
    "Dog":[n-1,N-n,N-1],
    "Msos":[Msstr,Msse,"--"],
    "Vr":[Fcal,"~F(n-1)(N-n)", "--"]
}
d=pd.DataFrame(ANOVA)
print(d)
if(Fcal<1):
    Fcal=1/Fcal
Ftab=round((ss.f.ppf(1-alpha,n-1,N-n)),3)
print("Ftab:",Ftab)
if(Fcal<Ftab):
    print("Accept H0")
else:
    print("Reject H0")

    
#90,82,79,98,83,91
#105,89,93,104,89,95,86
#83,89,80,94
