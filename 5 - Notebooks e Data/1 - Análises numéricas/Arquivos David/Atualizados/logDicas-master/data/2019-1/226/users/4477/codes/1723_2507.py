# Entradas
QI = int(input("Determine o valor: "))
CA = int(input("Determine o valor: "))
QV = int(input("Determine o valor: "))
# Percentual
PerCA = CA / 100 
# Variavel contadora
mes = 0

# laço
while (QI > 0 and QI < 8000):
	QI = (QI + (QI * PerCA)) - QV       #Acumula numero de peixes
	mes = mes + 1                       #Atualiza numero de meses
	#Condicoes
	if (QI >= 8000):
		print ("MAXIMO")
	elif (QI <= 0):
		print ("ZERO")
	else:
		QV = int(input("Num mmensal de peixes: "))
# Saida
print(mes)