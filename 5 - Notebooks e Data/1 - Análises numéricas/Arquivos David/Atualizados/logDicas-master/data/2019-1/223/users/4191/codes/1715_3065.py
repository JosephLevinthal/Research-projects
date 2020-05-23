T=input("Tipo de ataque: ").upper()
V=int(input("Valor do dado: "))
N=int(input("Numero de turnos recebendo dano: "))
if((V<1)or(V>4)or(T!='CAUDA')and(T!='CUSPE')and(T!='PATADA')):
	print('Entrada invalida')
elif(T=='CAUDA'):
	dano= V * N
	print(dano)
elif(T=='CUSPE'):
	dano= 2*V*N
	print(dano)
elif(T=='PATADA'):
	dano=2*V+5*N
	print(dano)
	