from numpy import *
a = int(input("digite n: "))
b = "*"
for i in range(a):
	c = b*(a-i)
	print(c)
for i in range(a+1):
	c = b*(a-(a-i))
	print(c)