n = int(input("valor aproximado de pi: "))

# Variavel contadora
cont = 1

# Variavel acumuladora
aprox = 3

while ( cont < n ):
	# Denominador
	x = (cont * 2) * (cont * 2 + 1) * (cont * 2 + 2)
	
	# Aproximacoes de PI
	aprox = aprox + (-1) ** (cont + 1) * 4 / x
	cont = cont + 1

print (round(aprox,8))
	
	
	




