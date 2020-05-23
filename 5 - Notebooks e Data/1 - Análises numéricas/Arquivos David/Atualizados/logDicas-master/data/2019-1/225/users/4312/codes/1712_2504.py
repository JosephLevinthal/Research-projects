qv = int(input("Insira a quantidade de virus: "))
ql = int(input("Quantidade inicial de leucocitos: "))
pv = float(input("Insira o percentual  de virius: "))
pl = float(input("Insira o percentual de leucocitos: "))

i = 0  #Var. Cont.

while(ql < 2 * qv):
	x = qv * pv / 100
	qv = qv + x
	y = ql * pl / 100
	ql = ql + y
	i = i + 1
	if(ql >= 2 * qv):
		print(i)	
	
	
	