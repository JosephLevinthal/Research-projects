#entrada de um numero inteiro
z = int(input("Digite um numero inteiro: "))
i = 0
div = 0
while (i <= z):
	r = z%(i + 1)
	if (r == 0):
		print(i+1)
		div = div + 1
	i = i+1
if (div == 1):
	print(1,"divisor")	
else:
	print(div, "divisores")