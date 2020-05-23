n = int(input("Insira o valor de n: "))

i = 0
d = 0
soma = 0
while(i < n/2):
	i = i + 1
	if((n%i) == 0):
		print(i)
		soma = soma + i
if(soma == n):
	print("PERFEITO")
else:
	print("NAO PERFEITO")