qip = int(input())
qiv = int(input())
pap = float(input())
pav = float(input())

lim = qiv + qip
anos = 0

while (lim <= 80000):
	c1 = qip*pap/100
	qip = qip + c1
	c2 = qiv*pav/100
	qiv = qiv + c2
	anos = anos + 1
print(anos)