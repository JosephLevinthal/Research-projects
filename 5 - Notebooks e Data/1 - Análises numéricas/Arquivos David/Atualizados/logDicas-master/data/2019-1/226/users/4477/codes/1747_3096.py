# Entradas
pc = int(input("Determine pc: "))
# Variaveis
soma = 0
# Laco
while (pc != 0):
	
	pc = int(input("Determine pc: "))
	
	if (pc == 1):
		soma = soma + 20
	elif (pc == 2):
			soma = soma + 15
	elif (pc == 3):
		soma = soma + 10
	elif (pc >= 4 or pc <= 10):
		soma = 11 - pc

print(soma)