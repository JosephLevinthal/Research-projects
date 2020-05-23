n = int(input("Digite o numero de termos: "))
pi = 3
i = 2
cont = 0
if n == 1:
	print(3.0)
else:
	while cont < n-1:
		sinal = (-1) ** cont
		pi = pi + sinal * ((4) / ((i) * (i+1) * (i+2)))
		cont = cont + 1
		i = i+ 2
	print(round(pi, 8))
	
