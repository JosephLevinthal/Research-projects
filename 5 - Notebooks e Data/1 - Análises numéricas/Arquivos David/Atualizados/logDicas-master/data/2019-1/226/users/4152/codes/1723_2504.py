qv = int(input("Quantidade inicial de copias do virus no sangue de Micaleteia: "))
ql = int(input("Quantidade de leucocitos no sangue: "))
pv = int(input("Percentual de multiplicacao diaria do virus: "))
pl = int(input("Percentual de multiplicacao diarias de leucocitos: "))
p1 = pv / 100
p2 = pl / 100
a = 0
while (qv*2 > ql):
	ql = ql + (ql * p2)
	qv = qv + (qv * p1)
	a = a + 1
print(a)