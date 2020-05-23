m = int(input("digite o numero do movimento da lagartixa: "))
soma = 0
while m != 0:
	soma = soma + m
	m = int(input("digite: "))
if soma > 0:
	print(soma)
	print("Acima")
elif soma == 0:
	print(soma)
	print("Inicial")
else:
	print(soma)
	print("Abaixo")