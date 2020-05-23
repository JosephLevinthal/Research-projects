from numpy import *
i=1
c=input()
h=0
if(c=="Calcule"):
	while i <=50:
		h=(i+2)/i +h
		i=i+1
h=h+1
h=h+35.5
print(round(h,2))
		