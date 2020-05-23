habA = int(input("Numeros de habites da cidade A:"))
habB = int(input("Numeros de habites da cidade B:"))
pcresA = float(input("Percentual de crescimento da cidade A:"))
pcresB = float(input("Percentual de crescimento da cidade B:"))

anos = 0 
while(habA < habB):
	habA = habA + (habA * (pcresA/100))
	habB = habB + (habB * (pcresB/100))
	anos = anos + 1
	
print(anos)