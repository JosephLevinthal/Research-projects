n = int(input("Numero inteiro: "))
a = 1
soma = 0
while(a < n):
	b = n%a
	if(b==0):
		print(a)
		soma = a + soma
	a = a + 1
if(soma == n):
	print("PERFEITO")
else:
	print("NAO PERFEITO")