import math
r = float(input("raio"))
x = float(input("ar"))
e = float(input("escolha"))
a = math.pi/3*(x**2)*(3 * r - x)
if (e == 1):
	v = a
else:
	v = 4/3*math.pi*(r**3) - a
print(round(v, 4))