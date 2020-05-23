from math import*
a = float(input("a:"))

if ((a >= -4) and (a < 0)):
	d = abs(a**(1/2))
elif (a == 0):
	d = 0
elif ((a > 0) or (a <= 4)):
	d = a**(1/2)
elif((a > 4) or (a < -4)):
	d = "entrada invalida"
	
print(round(d,4))