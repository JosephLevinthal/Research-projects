cont = 0
soma = 0
x = int(input("insira o numero:"))

while(x != -1):
	soma = soma + x
	cont = cont + 1
	x = int(input("insira o numero:"))
if(x == -1):
	print(soma)
