qnt1=int(input("quantidade inicial de pirarucus: "))
pc=int(input("percentual de crescimento: "))
por=pc/100
meses=0
while(0<qnt1<=8000):
	bye=int(input("quantidade peixes retirados: "))
	qnt1=(qnt1+qnt1*por)-bye
	meses=meses+1
if(qnt1<=0):
		print("ZERO")
		print(meses)
if(qnt1>=8000):
		print("MAXIMO")
		print(meses)
