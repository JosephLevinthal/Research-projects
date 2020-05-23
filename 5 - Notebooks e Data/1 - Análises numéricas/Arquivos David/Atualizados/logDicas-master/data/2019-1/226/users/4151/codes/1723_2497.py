qi=float(input("valor inicialmente investido: "))
meses=(int(input("meses de aplicacoes: "))
saldo= qi
t=0
i=0.04
		 
while(t<meses):
	saldo=saldo+(saldo*i)
	t=t+1
print(round(saldo,2))

	
