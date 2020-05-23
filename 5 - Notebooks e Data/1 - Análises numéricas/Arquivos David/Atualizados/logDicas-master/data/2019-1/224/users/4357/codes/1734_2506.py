qinicial=int(input("digite o numero:"))
pcrescimento=float(input("digite o numero:"))
qvenda=int(input("digite o numero:"))
pcrescimento=pcrescimento/100
ano=0
while(0<=qinicial<=12000):
	qinicial=(qinicial+qinicial*pcrescimento)-qvenda
	ano=ano+1
if(qinicial<=0):
	print("EXTINCAO")
	print(ano)
if(qinicial>=12000):
	print("LIMITE")
	print(ano)