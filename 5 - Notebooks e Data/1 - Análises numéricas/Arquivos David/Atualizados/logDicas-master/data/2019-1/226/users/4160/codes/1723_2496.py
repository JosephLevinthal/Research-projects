n = int(input("Digite um numero: "))

i = 0 
soma = 0 
while (n != -1):	
	i = i + 1
	soma = soma + n
	n = int(input("Digite um numero: "))	

if (n==-1):
	print(soma)