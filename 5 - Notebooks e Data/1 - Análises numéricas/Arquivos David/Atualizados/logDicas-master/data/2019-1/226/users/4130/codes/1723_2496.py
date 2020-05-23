cont = 0
soma = 0
x = int(input("Digite um numero: "))

while(x != -1):
	soma = soma + x
	cont = cont + x
	x = int(input("Digite um numero: "))
if(x == -1):
	print(soma)
	