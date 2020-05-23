#Leitura do numero inteiro
n = int(input("digite um numero com tres digitos: "))

#remocao do numero da esquerda e resto
r = n%100

if(n%r == 0):
	print("SIM")
else:	
	print("NAO")

