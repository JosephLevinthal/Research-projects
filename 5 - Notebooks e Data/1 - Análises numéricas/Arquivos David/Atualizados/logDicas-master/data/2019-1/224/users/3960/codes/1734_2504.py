virus = int(input("Quantidade inicial de copias do virus: "))
leucocitos = int(input("Quantidade inicial de leucocitos: "))
percVirus = float(input("Percentual de multiplicacao diaria do virus: "))
percLeucocitos = float(input("Percentual de multiplicacao diaria dos leucocitos: "))

dias = 0

while(leucocitos <= (virus*2)):
	virus = virus + virus * (percVirus / 100)
	leucocitos = leucocitos + leucocitos * (percLeucocitos / 100)
	dias = dias + 1
	
print(dias)