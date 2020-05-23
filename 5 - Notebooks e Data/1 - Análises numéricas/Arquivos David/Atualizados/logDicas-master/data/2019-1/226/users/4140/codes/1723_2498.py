haba=int(input())
habb=int(input())
prca=float(input())
prcb=float(input())

prca=prca/100
prcb=prcb/100
ano=0
while(haba<habb):
	crea=(haba*prca)//1
	haba=(haba+crea)
	creb=(habb*prcb)//1
	habb=(habb+creb)
	ano=ano+1
print(ano)