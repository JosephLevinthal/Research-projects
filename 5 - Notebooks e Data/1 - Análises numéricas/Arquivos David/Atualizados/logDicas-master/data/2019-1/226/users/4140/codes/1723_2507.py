qinicial=int(input())
cres=float(input())
i=0
while(qinicial<=8000 and qinicial>0):
	venda=int(input())
	soma=qinicial*(cres/100)
	qinicial=qinicial+soma-venda
	i=i+1
if(qinicial<=0):
	print("ZERO")
	print(i)
if((qinicial>=8000)):
	print("MAXIMO")
	print(i)
