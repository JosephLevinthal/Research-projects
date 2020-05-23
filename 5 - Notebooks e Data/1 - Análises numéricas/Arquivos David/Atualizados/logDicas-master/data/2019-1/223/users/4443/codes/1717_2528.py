#Digito de um numero inteiro positivo
num = int(input("Digite um numero inteiro positivo: "))	

while(num != -1):
	z =  num
	soma = 0
	while (z > 0):
		pot = len(str(num))
		unidade = z%10
		soma = soma + unidade**pot
		z = z//10
	if(num == soma):	
		print("ARMSTRONG")
	else:
		print("NAO ARMSTRONG")
	num = int(input("Digite um numero inteiro positivo: "))

