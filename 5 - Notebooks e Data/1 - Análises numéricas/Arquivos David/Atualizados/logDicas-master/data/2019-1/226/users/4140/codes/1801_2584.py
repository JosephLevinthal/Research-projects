from numpy import*
from math import*
n=int(input())
soma=0
for i in range(2,n+1):
	soma=(((-1)**(i-1))*1)/i + soma 
soma=soma+1	
print("H =",round(soma,6))