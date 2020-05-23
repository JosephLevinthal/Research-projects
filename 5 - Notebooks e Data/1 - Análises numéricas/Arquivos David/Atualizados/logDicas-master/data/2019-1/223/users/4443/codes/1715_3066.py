#Leitura dos dados: pontos de vida e valores dos dados sorteados
v = int(input("Digite a quantidade inicial de pontos de vida: "))
p1 = int(input("Digite o valor do primeiro sorteio: "))
p2 = int(input("Digite o valor do segundo sorteio: "))
p3 = int(input("Digite o valor do terceiro sorteio: "))

if(1 <= p1 <= 12) and (1 <= p2 <= 12) and (1 <= p3 <= 12) and (v >= 0):
	pvr = v - (10*(p1+p2+p3))
	if(pvr > 0):
		print(pvr)
		print("VIVO")
	else:
		print(0)
		print("MORTO")
else:
	print("Entrada invalida")
