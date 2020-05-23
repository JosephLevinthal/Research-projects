from math import *
n = int(input("repeticao: "))
d = sqrt(12) #constante
y = 1 #variavel do denominador
i = 0 #expoente
soma = 0 #soma dos termos
c=0 #var
h=0
while (c < n):
	if (n > 1):
		h = ((-1)**i / (y * (3**i)))*d
		
	else: 
		soma = d
	i = i + 1
	y = y + 2
	soma = soma + h
	c=c+1
print(round(soma, 8))
		