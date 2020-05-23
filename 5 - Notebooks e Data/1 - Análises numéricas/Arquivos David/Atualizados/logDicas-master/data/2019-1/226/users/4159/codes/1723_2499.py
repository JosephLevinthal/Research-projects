from math import*
k = float(input("numero: "))
n = 1
e = 1
while(n<k):
	e = e + 1/factorial(n)
	n = n+1
print(round(e, 8))
	