from numpy import *

num=int(input("..."))

v=arange(num)
for i in range(size(v)):
	v[i]=v[i]+1
b="*"
i=-1
cont=0
while(cont!=size(v)):
	print('*'*v[i])
	i=i-1
	cont=cont+1
	
for i in range(size(v)):
	print('*'*v[i])
