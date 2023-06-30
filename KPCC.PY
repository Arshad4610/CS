import numpy as np
x=[float(x) for x in input().split(',')]
y=[float(y) for y in input().split(',')]
x=np.array(x)
y=np.array(y)
n=len(x)
sumx=sum(x)
sumxx=sum(x*x)
xbar=sumx/n
sumy=sum(y)
sumyy=sum(y*y)
ybar=sumy/n
sumxy=sum(x*y)
cov=(1/n)*sumxy-(xbar*ybar)
print("covariance is:",cov)
sigma_x=((1/n)*sumxx-xbar**2)**0.5
sigma_y=((1/n)*sumyy-ybar**2)**0.5
r=cov/(sigma_x*sigma_y)
print("r=",r)
