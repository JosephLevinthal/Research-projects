n = int(input("numero: "))
d = 1 #variavel do denominador
soma = 0 #acumuladora
cont = 0  #contadora
i = 0 #expoente
s = 0
while (cont < n):
	if (n > 1):
		s = (-1)**i * (4 / d)
	else:
		soma = 4
	i = i + 1
	d = d + 2
	soma = soma + s
	cont = cont + 1
print(round(soma, 8))
		

