from math import*

r = float(input())
a = float(input())
n = int(input())

va = (4*(pi)*(r**3))/3
vc = ((pi)*(a**2)*(3*r-a))/3
com= va-vc
if(n == 1):
	print(round(vc,4))
if(n == 2):
	print(round(com,4))