from math import factorial 
k = int(input(""))
x = 1
e = 1
while x < k:
	e += 1/factorial(x)
	x = x + 1
e = round(e, 8)
print(e)