from math import*

x = float(input("Digite x: "))

if(x <= -1 or x >= 1):
	v = x**(1/2)
elif(x > -1 and x < 0 or x > 0 and x < 1):
	v = x
elif(x == 0):
	v = 0

print(round(abs(v),2))