j=float(input())
valor=float(input())
qf=1500*(1+j)**36

if (qf>=valor):
	print(round(qf,2))
	print('Sim')
else:
	print(round(qf,2))
	print('Nao')