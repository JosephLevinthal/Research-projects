from math import*

x = float(input())

if(x <= -1) or (x >= 1):
	print(round(abs(x) ** (1 / 2), 2))
elif((-1 < x or x < 0) or (0 < x or x < 1)) and x != 0:
	print(round(abs(x), 2))
else:
	print(0)