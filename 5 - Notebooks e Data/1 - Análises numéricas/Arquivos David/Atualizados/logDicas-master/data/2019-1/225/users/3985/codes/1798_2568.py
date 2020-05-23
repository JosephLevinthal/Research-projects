from numpy import*

v = array(eval(input()))
b = 0
c = 0
for i in range(v, 0, -1):
	b = "*" * i + ("o" * 2 * c) + i * "*"
	c = c + 1
	print(b)