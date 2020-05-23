#Leitura de valores:
rs = float(input("Qual o valor disponivel? "))
nru = int(input("quantidade de tickets do RU: "))
vru = float(input("Qual o valor dos tickets? "))
nbus = int(input("quantidade de passes: "))
vbus = float(input("Qual o valor dos passes? "))

#Verificação dos valores
calc = (nru*vru) + (nbus*vbus)
if (calc <= rs):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")
	
	
