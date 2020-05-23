from numpy import *
a = array(eval(input()))
b = array(eval(input()))
c = int(input("carga: "))
v = zeros(3, dtype=int)
for i in range(size(a)):
	if(a[i]>=5 and b[i]>= 0.75*c):
		v[0]=v[0]+1
	elif(a[i]<5 and b[i]>=0.75*c):
		v[1]=v[1]+1
	else:
		v[2]=v[2]+1
print(v)