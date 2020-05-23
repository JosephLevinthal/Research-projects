from numpy import *
n=int(input())
soma=0
for i in range(1,n):
	soma=(1/(i+1))+soma
soma=soma+1	
print(round(soma,2))