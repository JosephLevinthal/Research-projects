
consumo = int(input())

if (consumo <= 150):
	valor = ((0.60 * consumo) + 5)
else:
	valor = ((0.75 * consumo) + 16)
	
print(valor)