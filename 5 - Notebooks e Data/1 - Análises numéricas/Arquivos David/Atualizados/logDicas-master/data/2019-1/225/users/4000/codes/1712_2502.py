from math import*
n = int(input())
c = 0
d = 1
e = 0
aux = 1
while(c<n):
	e = e + (aux * (1 / (d *(3**c))))
	if(aux ==1):
		aux = -1
	else:
		aux = 1
	c = c+1
	d = d+2
e = e *sqrt(12)
print(round(e,8 ))