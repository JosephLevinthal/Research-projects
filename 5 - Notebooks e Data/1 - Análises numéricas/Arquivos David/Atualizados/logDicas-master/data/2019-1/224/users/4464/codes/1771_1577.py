from numpy import *


a = float(input("insira a acelera, men: "))
v0 = float(input("insira a v0 do car, men: "))
n = int(input("insira um numero positivo: "))

t = array(arange(n))
cont = 0
d = zeros(n)

while (cont < (size(d))):
	d[cont] = ((a*t[cont]**2)/2) + v0 * t[cont]
	cont+=1
print(d)

