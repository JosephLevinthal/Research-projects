from numpy import *
n = input("digite: ").upper()
i=n.replace(" ","")
a = 0
b = -1
while(a < len(i)):
	if (i[a]==i[b]):
		c=1
	if (i[a]!=i[b]):
		c=0
	a = a + 1
	b = b - 1
print(i)
print(c)
		
	