from numpy import*
v = array(eval(input("Entrada: ")))
a = 0
n = 0
for i in range(v, 0, -1):
	a = "*" * i + ("o" * 2 * n) + i * "*"
	n = n + 1
	print(a)
