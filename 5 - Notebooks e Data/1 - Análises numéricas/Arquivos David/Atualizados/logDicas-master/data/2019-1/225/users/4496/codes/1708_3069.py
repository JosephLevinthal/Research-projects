atq = input("Digite o nome do ataque: ").upper()
fd1 = int(input("Digite o numero do dado 1: "))
fd2 = int(input("Digite o numero do dado 2: "))


FURIA = (10)
GRITO = (6)
TOQUE = ((fd1+fd2) **2)
d8 = (fd1 + fd2)

if(atq == FURIA):
	total = (10 + d8)
	print(total)
elif(atq == GRITO):
	total = (6 + d8)
	print(total)
elif(atq == TOQUE):
	total = (d8**2)
	print(total)
else:
	print("Entrada invalida")
