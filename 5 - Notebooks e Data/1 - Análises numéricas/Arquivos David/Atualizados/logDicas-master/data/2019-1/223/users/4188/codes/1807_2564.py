from numpy import *
a = array(eval(input("n.gols: ")))
b = array(eval(input("gols.ad: ")))
c = zeros(3,dtype=int)
for i in range(size(a)):
	if(a[i]>b[i]):
		c[0] = c[0] + 1
	if(a[i]==b[i]):
		c[1] = c[1] + 1
	if (a[i] < b[i]):
		c[2] = c[2] + 1
print(c)