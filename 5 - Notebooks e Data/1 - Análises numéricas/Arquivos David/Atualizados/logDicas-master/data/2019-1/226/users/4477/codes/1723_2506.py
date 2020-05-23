# Entradas
QI = int(input("Determine o valor: "))
CA = int(input("Determine o valor: "))
QV = int(input("Determine o valor: "))
# Percentual
PerCA = CA / 100 
# Variavel contadora
ano = 0
# laço
while (QI > 0 and QI <12000):
	QI = (QI + (QI * PerCA)) - QV
	ano = ano + 1
#Condição
if (QI < 0):
	print ("EXTINCAO")
if (QI > 12000):
	print ("LIMITE")
#Saida
print(ano)
	