qv = int(input("Quantidade inicial de copias: "))
ql = int(input("Quantidade inicial de leucocitos: "))
pv = float(input("Percentual de multiplicacao do virus: "))/100
pl = float(input("Percentual de multiplicacao dos leucocitos: "))/100

dias = 0
while(ql < (2 * qv)):
	ql = ql + (ql * pl)
	qv = qv + (qv * pv)
	dias = dias + 1
print(dias)

	 
	
	
