cont = 0
soma = 0
n = int(input("Insira o numero: "))

while ((n != -1)):
	cont = cont + 1
	soma = soma + n
	n = int(input("Insira o numero: "))
if(n == -1):
	print(soma)