qi = int(input("q1: "))
qil = int(input("q1l: "))
pv = int(input("pv: "))
pl = int(input("pl: "))

dia = 0

while(qil <= 2 * qi):
	qi = qi + qi*(pv/100)
	qil = qil + qil*(pl/100)
	dia = dia + 1
	
print(dia)