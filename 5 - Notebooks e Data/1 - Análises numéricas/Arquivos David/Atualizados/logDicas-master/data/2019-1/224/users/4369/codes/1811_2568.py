v = int(input("Digite um numero: "))
for i in range(v):
	print("*" * (v - i) + "o" * i + "o" * i + "*" * (v -i))