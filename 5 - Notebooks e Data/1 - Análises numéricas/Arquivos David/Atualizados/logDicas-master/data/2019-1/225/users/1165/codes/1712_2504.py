qv = int(input("Quantidade virus: "))
ql = int(input("Quantidade de leucocitos: "))
pv = float(input("Perc virus:"))
pl = float(input("Perc leucocitos: "))

t = 0

while (ql < 2 * qv):
	q = qv * pv/100
	qv = qv + q
	q2 = ql * pl/100
	ql = ql + q2
	t = t + 1
	if (ql >= 2 * qv):
		print(t)
	