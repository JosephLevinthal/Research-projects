from numpy import *
a = array(eval(input("meia: ")))
b = array(eval(input("frequencia: ")))
d = int(input("carga: "))
c = zeros(3,dtype=int)
for i in range(size(a)):
	if(a[i] >= 5 and b[i] >= 0.75*d):
		c[0] = c[0] + 1
	if(a[i] < 5 and b[i] >= 0.75*d):
		c[1] = c[1] + 1
	if( b[i] < 0.75*d):
		c[2] = c[2] + 1
print(c)
	
	
	