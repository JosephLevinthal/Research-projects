qip=int(input("quantidade de inicial: "))
pc=float(input("percentual de crescimento: "))
pcc=pc/100
c=0
while(0<qip<=8000):
	qpr=int(input("pirarucu retirados: "))
	r=qip*pcc
	qip=qip+r-qpr
	c=c+1
if(qip<=0):
	print("ZERO")
	print(c)
elif(qip>=8000):
	print("MAXIMO")
	print(c)