HA = int(input("Numero de habitantes da cidade A: "))
HB = int(input("Numero de habitantes da cidade B: "))
PA = float(input("Percentual de crescimento populacional da cidade A: "))/100
PB = float(input("Percentual de crescimento populacional da cidade B: "))/100

# HA < HB || PA > PB

ano = 0
qhabA = 0
qhabB = 1

while HA < HB:
	HA = HA + HA*PA
		
	HB = HB + HB*PB
	
	ano = ano+1
	
print(ano)