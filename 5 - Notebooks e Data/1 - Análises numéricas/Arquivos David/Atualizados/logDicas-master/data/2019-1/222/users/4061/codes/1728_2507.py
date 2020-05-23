quantinicial = int(input("digite quantidade inicial: "))
percres = int(input("digite percentual de crescimento: "))
#quantmes = int(input("digite quantidada mensal: "))
#quantret = int(input("digite quantidade retirada: ")) 
quantvenda = int(input("digite quantidade de venda: "))

pirarucus = 0
meses = 0

while(quantinicial > 0):
	pirarucus = pirarucus + meses
	meses = meses + 1
	if(quantinicial > 0):
		print("MAXIMO")
	else:
		print("ZERO")
	