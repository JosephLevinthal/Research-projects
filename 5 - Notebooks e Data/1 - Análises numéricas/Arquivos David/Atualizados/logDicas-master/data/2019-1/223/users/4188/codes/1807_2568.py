from numpy import *
a = int(input("valor: "))
b = "*"
c= "o"
for i in range(a):
	d = (b*(a-i))+(c*(a-(a-i)))+(c*(a-(a-i)))+(b*(a-i))
	print(d)
	