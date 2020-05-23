n = int(input("Insira um numro inteiro: "))
for i in range(n):
	msg = (n - i)*"*" + i*"o" + i*"o" + (n - i)*"*"
	print(msg)