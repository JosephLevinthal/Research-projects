# Entradas
NHA = int(input("Determine A: "))              # Número de habitantes de uma cidade A
NHB = int(input("Determine B: "))              # Número de habitantes de uma cidade B
PCA = float(input("Percentual de A: "))        # Percentual de crescimento populacional da cidade A
PCB = float(input("Percentual de B: "))        # Percentual de crescimento populacional da cidade B
# Percentual
percA = PCA / 100                              # Percentual de crescimento de A
percB = PCB / 100                              # Percentual de crescimento de B
# Variavel Contadora
ano = 0 
# Laco de acumulação
while (NHA < NHB):
	NHA = NHA + (NHA * percA)
	NHB = NHB + (NHB * percB)
	ano = ano + 1
# Saida
print (ano)