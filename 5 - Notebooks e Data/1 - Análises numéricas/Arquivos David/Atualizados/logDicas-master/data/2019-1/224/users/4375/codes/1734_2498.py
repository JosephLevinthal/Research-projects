ha=int(input("numero de hab da cidade a: "))
hb=int(input("numero de hab da cidade b: "))
pa=float(input("percentual a: "))
pb=float(input("percentual b: "))
tca=pa/100 
tcb=pb/100
anos=0
ppa=ha
ppb=hb
while(ppb>ppa):
	ca=ppa*tca
	cb=ppb*tcb
	ppa=ppa+ca
	ppb=ppb+cb
	anos=anos+1
print(anos)

#taxa de crescimento = percentual de crescimento/100
#crescimento = numero de habitantes *taxa de crecimento
#ercentual de crescimento= percentual de crescimento+crescimento
