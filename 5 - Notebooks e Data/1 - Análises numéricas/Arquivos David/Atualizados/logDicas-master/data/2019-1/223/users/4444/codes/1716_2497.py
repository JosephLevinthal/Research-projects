vo = float(input("Quantia inicial: "))
qdtmeses= int(input("Tempo de investimento: "))
contador = 1 #variaval contadora registra os meses transcorridos
while(contador <= qdtmeses):
	acres = vo * 0.04
	vo = vo + acres
	contador = contador + 1
	print(round(vo,2))


	
