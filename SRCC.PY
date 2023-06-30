def rank(a):
    n=len(a)
    ranks=[]
    for i in range(n):
        big=1
        same=0
        for j in range(i):
            if(a[j]>a[i]):
                big+=1
            if(a[j]==a[i]):
                same+=1
        for j in range(i+1,n):
            if(a[j]>a[i]):
                big+=1
            if(a[j]==a[i]):
                same+=1
        ranks.append(big+same*0.5)
    return ranks
def CF(a,b):
    cf=0
    ma,fx=np.unique(a,return_counts=True)
    mb,fy=np.unique(b,return_counts=True)
    for i in range(len(ma)):
        if(fx[i]>1):
            cf+=(fx[i]*((fx[i]**2)-1))/12
    for i in range(len(mb)):
        if(fy[i]>1):
            cf+=(fy[i]*((fy[i]**2)-1))/12
    return cf
def srcc(x,y):
    if(len(x)!=len(y)):
        print("INVALID")
    rank_x=rank(x)
    rank_y=rank(y)
    di=np.subtract(rank_x,rank_y)
    di2=di**2
    sumdi2=sum(di2)
    n=len(x)
    cf=CF(x,y)
    sumdi2+=cf
    srcc=1-((6*sumdi2)/(n*(n**2-1)))
    print("spearman's rank correlation coefficient is: ",srcc)
x=[float(x) for x in input().split(',')]
y=[float(y) for y in input().split(',')]
srcc(x,y)



#68,64,75,50,64,80,75,40,55,64
#62,58,68,45,81,60,68,48,50,70
