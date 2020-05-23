s = float(input("Qual salario bruto: "))
#Aliquota
d1 = s - (s*(8/100))
d2 = s - (s*(9/100)) 
d3 =  s - (s*(11/100))
d4 = s - 608.44


if s < 1659.38 :
	a1 = round(d1,2)
	print("Salario liquido = R$  ", a1)
elif ((s >= 1659.39) and (s < 2765.66)):
	if ((d2 < 1903.98) and (d2 <)
	