dia = 0
qiv = int(input("Digite a quantidade inicial de copias do virus: "))
qil = int(input("Digite a quantidade inicial de leucocitos: "))
pmv = int(input("Digite o percentual de multiplicacao do virus: "))
pml = int(input("Digite o percentual de multiplicacao dos leucocitos: "))
dia = 0
while (qil < 2*qiv):
	dia = dia + 1
	qil = qil + (qil*pml)/100
	qiv = qiv + (qiv*pmv)/100
print(dia)