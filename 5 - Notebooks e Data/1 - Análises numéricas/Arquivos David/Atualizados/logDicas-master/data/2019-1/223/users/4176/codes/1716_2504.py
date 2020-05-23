qic = int(input("Quant. de copias: "))
qil = int(input("Quant. de leucocitos: "))
pmv = int(input("Percentual de mult. do virus: "))
pml = int(input("Percentual de mult. dos Leuc.: "))

d = 0

while ( qic > qil/2):
	qic = qic + ( qic * ( pmv/100 ))
	qil = qil + ( qil * ( pml/100 ))
	d = d + 1
print(d)