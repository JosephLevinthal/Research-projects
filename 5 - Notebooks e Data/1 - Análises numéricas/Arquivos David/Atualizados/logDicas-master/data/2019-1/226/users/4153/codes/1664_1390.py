from math import*
c = float(input("Insira o consumo de mins: ")) #consumo de minutos do cliente
C = abs(c)
if(C <= 100):
	v = C * 1.20  #Valor da conta
else:
	v = (C * 1.40) + 25.0
print(round(v, 2))