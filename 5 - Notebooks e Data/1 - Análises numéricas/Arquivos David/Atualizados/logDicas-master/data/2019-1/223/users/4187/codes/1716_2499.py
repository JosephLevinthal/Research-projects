from math import*
k1 = int(input("Digite valor de k:"))
v = 0
e = 0
while(v < k1):
	e = e + (1/factorial(v))
	v = v + 1
print(round(e,8))

