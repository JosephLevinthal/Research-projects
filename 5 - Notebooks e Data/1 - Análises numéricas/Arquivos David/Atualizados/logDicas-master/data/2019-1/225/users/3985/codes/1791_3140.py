from numpy import*
v=array(eval(input()))
i=0
p=5*(size(v))
n=sum(v)/size(v)
l=1/5
M=((sum(v[i])**p)/n)**(1/5)
m=round(M,2)
print(m)