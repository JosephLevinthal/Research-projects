from numpy import *
from math import*
x=float(input())
k=int(input())
cos=0
for i in range(2,k*2,2):
	cos=((x)**i)/factorial(i) +cos
cos=cos+1
print(round(cos,8))
	