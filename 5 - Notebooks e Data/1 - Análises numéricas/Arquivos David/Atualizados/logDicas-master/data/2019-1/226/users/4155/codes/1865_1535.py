from math import*
x = float(input("v: "))
k = int(input("k: "))
i = 0
a = 0
while(x >= -1 and x <= 1 and k > 0):
	x = x + ((-1)**i) * (x**(2*i+1)/(2*i+1))
	i = i + 1
	print(round(x, 6))
	