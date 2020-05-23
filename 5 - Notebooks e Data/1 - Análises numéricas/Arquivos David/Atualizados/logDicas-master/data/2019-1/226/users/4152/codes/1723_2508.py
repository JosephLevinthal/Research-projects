n = int(input("Digite aqui o valor de n: "))
a = 0 #Contadora
x = 2
y = 3
z = 4
s = 2
soma = 0
while (a < n):
	p = 3 + soma
	soma = soma + ((4 /(x * y * z)) * ((-1) ** s))
	x = x + 2
	y = y + 2
	z = z + 2
	s = s + 1
	a = a + 1
print(round(p, 8))