n=int(input("capacidade: "))
e=int(input("estoque: "))
q=int(input("quantidade: "))
sem=0
while(e >0 ):
	e=e -n + q
	sem=sem+1
print(sem)
	