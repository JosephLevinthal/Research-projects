from math import*
n=float(input("numero n: "))
pia=sqrt(12)
c=0
i=1
d=0
soma= 0
if (n==1):
	print(round(sqrt(12), 8))
else:
	while (c<n):
		sinal= (-1)**c
		soma= soma+ (sinal* ((1)/(i*(3**d))))
		c=c+1
		i=i+2
		d=d+1
	pia= pia* soma
	print(round(pia, 8))