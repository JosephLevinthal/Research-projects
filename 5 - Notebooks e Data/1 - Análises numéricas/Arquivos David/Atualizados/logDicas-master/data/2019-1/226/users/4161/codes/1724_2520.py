from math import*
n =int(input("serie: "))
pi = 0
v = 0
t = 0
while (t<n):
	pi = pi + 1/((1+t)**2)
	t = t + 1
pi = sqrt(6*pi)
print(round(pi, 6))