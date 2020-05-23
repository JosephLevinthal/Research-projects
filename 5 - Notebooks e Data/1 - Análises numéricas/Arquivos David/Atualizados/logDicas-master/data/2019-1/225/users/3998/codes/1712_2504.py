qic= int(input("quantidade inicial de copia: "))
qil= int(input("quantidade inicial de leucocitos: "))
pv= float(input("percentual de virus: "))
pl= float(input("percentual de leucocitos: "))

dias = 0

while ((qil / qic)<= 2):
	qic = qic +(qic * (pv/100))
	qil = qil +(qil * (pl/100))
	dias = dias + 1
print(dias)