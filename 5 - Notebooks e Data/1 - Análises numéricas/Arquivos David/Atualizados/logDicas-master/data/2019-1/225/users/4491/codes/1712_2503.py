n = int(input("termo geral: "))

c = 0 #contador geral
d = 1 #denominador
e = 0 #soma inicializadora em zero
aux = 1 #variavel auxiliar entre 1 e -1

while(c < n):
	e = e + (aux * (4 / d))
	if(aux == 1): 
		aux = -1
	else: 
		aux = 1
		
	c = c + 1
	d = d + 2
print(round(e, 8))
	