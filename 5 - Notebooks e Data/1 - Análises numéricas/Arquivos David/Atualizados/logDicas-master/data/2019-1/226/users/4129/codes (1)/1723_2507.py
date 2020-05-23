pira = int(input("Quantidade inicial de pirarucus: "))
perc = int(input("Percentual de crescimento: "))

mes = 0
perc = perc/100


while(pira > 0 and pira < 8000 ):
	venda = int(input("pirarucus vendidos :"))
	pira = pira + (pira*perc)
	pira = pira - venda
	mes = mes + 1
	if(pira <= 0):
		print("ZERO")
	elif(pira > 8000):
		print("MAXIMO")
	
print(mes)