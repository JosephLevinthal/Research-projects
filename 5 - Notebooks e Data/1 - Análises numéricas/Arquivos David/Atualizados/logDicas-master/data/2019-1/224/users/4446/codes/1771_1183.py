from numpy import *
#[1,3,-1,5,-1] ==> [1,3,5] [1,3,0]
v = array(eval(input("digite o vetor: ")))
i = 0
siz = 0 
while(i<size(v)):
	if(v[i]>0):
		siz = siz + 1
	i = i + 1
i2 = 0
i3 = 0
z = zeros(siz,dtype = int)
while(i3<siz):
	if(v[i2]>=0):
		z[i3] = v[i2]
		i2 = i2 + 1
		i3 = i3 + 1
	else:
		i2 = i2 + 1
		i3 = i3 + 0
print(z)