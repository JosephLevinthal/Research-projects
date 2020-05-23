n = int(input())

c = 0 # contador para percorrer o laco
d = 1 # denominador
e = 0 # soma inicializada com zero
aux = 1 # variavel auxiliar varia entre -1 e 1

while(c < n):
	e = e + (aux * (4 / d))
	if(aux == 1):
		aux = -1
	else:
		aux = 1
		
	c = c + 1
	d = d + 2
	
print(round(e, 8))