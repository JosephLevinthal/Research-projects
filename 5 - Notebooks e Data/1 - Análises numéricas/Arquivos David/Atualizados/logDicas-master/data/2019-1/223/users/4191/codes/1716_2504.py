qc=int(input("Quantidade inicial de copias do virus: "))
ql=int(input("Quantidade inical de leucocitos: "))
pv=int(input("Percentual da multiplicacao do vitus: "))
pl=int(input("Percentual de multiplicacao dos leucocitos: "))

cont=0
ql1=ql
qc1=qc


while(ql1/2<qc1):
	ql1=ql1 + ql1*pl/100
	qc1=qc1 + qc1*pv/100
	cont=cont+1

	
print(cont)	