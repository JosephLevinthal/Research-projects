from numpy import*
c = input("Caracteres: ")
n = ""
i = 0
a = 1
while (i < len(c)):
	if (a == 4):
		a = 1
		n = n + "."
	n = n + c[i]
	a = a + 1
	i = i + 1
print(n)

	