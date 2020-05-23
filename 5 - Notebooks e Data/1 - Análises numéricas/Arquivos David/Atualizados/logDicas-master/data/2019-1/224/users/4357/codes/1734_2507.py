qinicial=int(input("digite o numero:"))
pcrescimento=float(input("digite o numero:"))
pcrescimento=pcrescimento/100
mes=0
while(0<=qinicial<=8000):
	qnovo=int(input("digite o numero:"))
	qinicial=(qinicial+qinicial*pcrescimento)-qnovo
	mes=mes+1
	print(mes)
if(qinicial<=0):
	print("ZERO")
	print(mes)
if(qinicial>=8000):
	print("MAXIMO")
	print(mes)