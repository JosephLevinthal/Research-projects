NHA = int(input("No de hab da cidade A: "))
NHB = int(input("No de hab da cidade B: "))
PCPA = float(input("Percentual de Crescimento Pop.A: "))
PCPB = float(input("Percentual de crescimento Pop.B: "))

anos = 0

while ( NHA < NHB ):
	NHA = NHA + ( NHA * (PCPA / 100))
	NHB = NHB + ( NHB * (PCPB / 100))
	anos = anos + 1
	
print(anos)