n = int(input("Insira um numero: "))

i = 1
soma = 1

while (n % i == 0):  
	soma = soma + 1
	i = i 
	print(i)
if (n % i == 0):
	i = i
	print(i)
	
print(i,"divisores")
	
	
	