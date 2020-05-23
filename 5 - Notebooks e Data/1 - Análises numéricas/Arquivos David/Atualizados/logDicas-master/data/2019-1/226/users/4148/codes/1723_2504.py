qc = int(input("quant. inicial : "))
ql = int(input("quant. inicial: "))
pv = int(input("perc. virus: "))
pl = int(input("perc. leucocitos: "))

dia = 0

while(ql <= 2 * qv):
	qv = qv + (qv * (pv/100))
	ql = ql +(ql * (pl/100))
	dia = dia + 1
	
print(dia)