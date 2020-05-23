n = int(input("Digite um numero:"))

for i in range(n):
	print((n-i)*"*" + 2*i*"o"  + (n-i)*"*")