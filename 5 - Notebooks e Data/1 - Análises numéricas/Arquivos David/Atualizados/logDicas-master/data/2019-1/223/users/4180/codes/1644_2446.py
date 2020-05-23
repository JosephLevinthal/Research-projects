senha=int(input("Digite a senha por favor: "))
primeira=senha//100000
segunda=senha%100000//10000
terceira=senha%10000//1000
quarta=senha%1000//100
quinta=senha%100//10
sexta=senha%10
resto=(segunda+quarta+sexta) % (primeira+terceira+quinta)
if(resto==0):
	print("acesso liberado")
else:
	print("senha invalida")