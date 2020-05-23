n1 = int(input("N1: "))
n2 = int(input("N2: "))

produto = n1 * n2
diferenca = n2 - n1

if(produto == produto % 2  ):
	print(n1 + n2)
else:
	print(diferenca)