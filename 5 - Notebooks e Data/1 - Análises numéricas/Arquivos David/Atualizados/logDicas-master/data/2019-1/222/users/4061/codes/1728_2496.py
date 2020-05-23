num = int(input("digite numero: "))

cont = 0
soma = 0

while(num != -1):
	soma = soma + num
	cont = cont + 1
	num = int(input("digite numero: "))
	
if(cont > 0):
	print(soma)
	