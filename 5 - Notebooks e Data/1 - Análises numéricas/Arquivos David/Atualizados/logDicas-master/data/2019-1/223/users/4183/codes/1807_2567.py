from numpy import *
a = int(input("N: "))
st = "*"
for i in range(a):
	b = st*(a-i)
	print(b)
for i in range(a + 1):
	b = st*(a - (a - i))
	print(b)