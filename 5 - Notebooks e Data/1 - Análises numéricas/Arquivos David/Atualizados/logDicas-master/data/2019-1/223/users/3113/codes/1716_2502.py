from math import*
num=int(input(""))
va=sqrt(12)
i=0	
s=0
vd=va*1/(2*i+1)*(3**i)
f=0
w=1
while(s<num):
	f=vd-1/(2*w+1)*(3**w)
	f1=f*(-1)**i
	i=i+1
	s=s+1
	w=w+1
print(round(f,8))
