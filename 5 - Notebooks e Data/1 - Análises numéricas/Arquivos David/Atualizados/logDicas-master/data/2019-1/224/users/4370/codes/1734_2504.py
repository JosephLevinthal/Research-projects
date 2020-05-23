qiv = int(input("quantidade inicial de virus: "))
qil = int(input("quantidade inicial de leucocitos: "))
percv = float(input("percentual de crescimento do virus: "))
percl = float(input("percentual de crescimento do leucocito: "))
percv, percl = percv/100, percl/100
t = 0
while(2 * qiv > qil):
	qiv = qiv + qiv * percv
	qil = qil + qil * percl
	t = t + 1
print(t)