habA = int(input("Insira o numero de habitantes da cidade A: "))
habB = int(input("Insira o numero de habitantes da cidade B: "))
cresc_popA = float(input("Insira o percentual de crescimento populacional da cidade A: "))
cresc_popB = float(input("Insira o percentual de crescimento populacional da cidade B: "))

cont_habA = habA
cont_habB = habB
cont = 0

while(cont_habA < cont_habB):
	cont_habA = cont_habA + (cont_habA * cresc_popA / 100)
	cont_habB = cont_habB + (cont_habB * cresc_popB / 100)
	
	cont = cont + 1
	
print(cont)