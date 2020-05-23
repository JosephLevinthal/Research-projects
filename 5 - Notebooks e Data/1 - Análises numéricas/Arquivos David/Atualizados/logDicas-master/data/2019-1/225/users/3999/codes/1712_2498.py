Na=int(input("numero de hab A: "))
Nb=int(input("numero de hab B: "))
pA=(float(input("percentual A: ")))/100
pB=(float(input("percentual B: ")))/100
ano=0
while(Na<Nb):
	Na=Na+(Na*pA)
	Nb=Nb+(Nb*pB)
	ano=ano+1
print(ano)	