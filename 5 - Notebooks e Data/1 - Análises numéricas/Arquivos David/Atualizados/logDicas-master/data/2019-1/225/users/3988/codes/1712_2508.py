n = int(input())

c = 0
d = 0
e = 0
aux = -1

while(c < n):
	if(c == 0):
		e = e + 3
	else:
		e = e + (aux * (4 / (d * (d + 1) * (d + 2))))
		
	if(aux == 1):
		aux = -1
	else:
		aux = 1

	c = c + 1
	d = d + 2

print(round(e, 8))