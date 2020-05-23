valor = float(input())
qtdRU = float(input())
valorRU = float(input())
qtdbus = float(input())
valorbus = float(input())

despesas = (qtdRU*valorRU) + (qtdbus*valorbus)

if(valor<despesas):
	print("INSUFICIENTE")
else:
	print("SUFICIENTE")
