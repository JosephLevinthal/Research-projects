from math import*

x=float(input("valor: "))
exp = x**1/3
print(round(exp,4))

if(x > 0):
	print(round(exp,4))
if(0 < x <= 1):
	print(round(exp,4))