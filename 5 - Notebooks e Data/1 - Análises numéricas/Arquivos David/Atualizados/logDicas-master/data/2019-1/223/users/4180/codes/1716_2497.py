Valor   = float(input("Quantia inicial: "))
Mes = int(input("Tempo de investimento: "))
Tempo = 0
while(Tempo < Mes):
		Lucro = Valor * 0.04
		Valor = Valor + Lucro
		Tempo = Tempo + 1
		print(round(Valor, 2))





	
