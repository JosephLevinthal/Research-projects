from math import*
k=float(input("numero real k: "))
e= 0
c= 0
if (k==1):
	print(1.0)
else:	
	while (c < k):
		e= e+ ((1)/factorial(c))
		c= c+1
print(round(e, 8))
