n = int(input("insira: "))
f = int(input("insira: "))

div1 = 0
div2 = 0
cont = 1

while (cont < n or cont < f):
	if (n % cont == 0 and cont != n):
		div1 = div1 + cont
	if (f % cont == 0 and cont != f):
		div2 = div2 + cont
	cont += 1
print(div1)
print(div2)

if (div1 == f and div2 == n):
	print("AMIGOS")
else:
	print("NAO AMIGOS")