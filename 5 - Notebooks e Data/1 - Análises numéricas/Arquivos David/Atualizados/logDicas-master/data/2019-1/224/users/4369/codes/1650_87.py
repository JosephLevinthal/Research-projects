n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

n1 != n2
n1 != n3
n2 != n3

if(n1 < n2 and n1 < n3):
	print(n1)
elif(n2 < n1 and n2 < n3):
	print(n2)
else:
	print(n3)