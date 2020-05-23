qic = int(input("copias de virus: "))
qil = int(input("leucocitos iniciais: "))
pmv =int(input("percentual de multiplicacao(dia): "))
pml = int(input("percentual(leucocitos): "))

dias = 0
pmv = pmv / 100
pml = pml / 100
while (qil /qic) <= 2:
	qil = qil * pml + qil
	qic = qic * pmv + qic
	dias = dias + 1
print(dias)