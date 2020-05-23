qv = int(input("Qtd. inicial do virus: "))
ql = int(input("Qtd. inicial do leucocitos: "))
pv = float(input("Percentual do virus: "))
pl = float(input("Percentual dos leucocitos: "))
t = 0 
while (ql < 2 * qv):
	q = qv * pv/100
	qv = qv + q
	q2 = ql * pl/100
	ql = ql + q2
	t = t + 1
	if (ql >= 2 * qv):
		print(t)
	
	
	
	