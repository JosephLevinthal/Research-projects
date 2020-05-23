from math import*
x = eval(input("angulo: "))
k = int(input("serie: "))
n= 0
cos = 1
while (n<k-1):
	if (n%2 !=0):
		cos = cos +(x**(1+n))/factorial(2+2*n)
	else:
		cos = cos -(x**(1+n))/factorial(2+2*n)
	n+=1
print(round(cos,6))