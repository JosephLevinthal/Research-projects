from numpy import*
from math import*
x=eval(input())
k=int(input())
cos=0
i=1
while i<k:
	cos=cos+((-1)**i)*((x**(i*2))/factorial(i*2))
	i=i+1
cos=cos+1
print(round(cos,11))
	