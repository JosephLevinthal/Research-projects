n1 = int(input("Digite o numero: "))
n2 = int(input("Digite o numero: "))
n3 = int(input("Digite o numero: "))
if((n1 < n2) and (n1 < n3)):
	print(n1)
if((n2 < n1) and (n2 < n3)):
	print(n2)
if((n3 < n2) and (n3 < n1)):
	print(n3)