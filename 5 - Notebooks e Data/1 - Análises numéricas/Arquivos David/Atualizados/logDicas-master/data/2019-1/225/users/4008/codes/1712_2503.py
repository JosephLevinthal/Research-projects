n = int(input("leia o numero: "))
e = 0
c = 0
d = 1
aux = 1
while(c<n):
	e = e + (aux *(4 / d))
	if(aux == 1):
		aux = -1
	else:
		aux = 1
	c = c+1
	d = d+2
print(round(e, 8))
		 
