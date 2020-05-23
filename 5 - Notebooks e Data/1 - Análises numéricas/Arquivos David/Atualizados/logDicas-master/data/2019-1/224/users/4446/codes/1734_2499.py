from math import factorial
k=int(input("digite k: "))
i=0
s= 0
while (i<k):
	s= s + 1 / factorial(i)
	i= i + 1
print(round(s, 8))

	