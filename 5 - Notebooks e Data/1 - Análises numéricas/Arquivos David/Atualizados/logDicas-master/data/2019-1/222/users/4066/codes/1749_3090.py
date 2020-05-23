num = int(input("Numero: "))

soma = 0

while (num != 0):
	soma = soma + num
	num = int(input("Numero: "))
	
print(soma)

if (soma < 0):
	print("Abaixo")
elif(soma == 0):
	print("Inicial")
elif(soma > 0):
	print("Acima")