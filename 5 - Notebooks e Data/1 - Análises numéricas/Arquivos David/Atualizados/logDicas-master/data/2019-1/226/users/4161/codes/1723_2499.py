from math import*
k = int(input("numero: "))
t = 1
e = 1.0
if k == 1:
	print(e)
else:
	while (t<k):
		e = e + 1/factorial(t)
		t = t + 1
print(round(e, 8))