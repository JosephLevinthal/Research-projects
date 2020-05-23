n = int(input("Digite o numero de termo"))

# Variavel contadora
cont = 1

# Variavel acumuladora
aprox = 3

while (cont < valor):
	# Denominador
	x = (cont * 2) * (cont * 2 + 1) * (cont * 2 + 2)
	
	# Novos termos de PI
	aprox = aprox + (-1) ** (cont + 1) * 4 / x
	cont = cont + 1

print (round(aprox,8))