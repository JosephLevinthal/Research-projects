from math import*
x = float(input("variavel x: "))

if x <= 0:
	y = 0
elif x > 0 and x <= 1:
	y = 1
elif x > 1 and x <= 2:
	y = abs(x) ** (1/2)
else:
	y = abs(x) ** (1/3)
	
print(round(y, 4))	