qiv = int(input("quantidade inicial de copias do viros: "))
qil = int(input("quantidade inicial de leucocitos: "))
pv = int(input("percentual do virus: "))
pl = int(input("percentual de leucocitos: "))

pov = pv / 100
pol = pl / 100

dia = 0

while (qil/2<qiv):
	
	qiv = qiv + (qiv * pov)
	qil = qil + (qil * pol)
	dia = dia + 1

print(dia)