num = int(input("Digite o numero: "))
cont = 0
soma = 0

while(num != -1):
	soma = soma + num
	cont = cont + 1
	num = int(input("Digite o numero: "))
	
print(soma)
