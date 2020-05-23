from numpy import*

a = array(eval(input("Entrada: ")))
c = 0
soma = sum(a) - c

for i in range(sum(a)):
	b = "*" * soma
	c = c + 1
	print(b)
	soma = sum(a) - c
c = sum(a) - 1
soma = 1
for i in range(sum(a)):
	b = "*" * soma
	c = c - 1
	print(b)
	soma = sum(a) - c