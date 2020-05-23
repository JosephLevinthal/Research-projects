from math import*
k=int(input("entre com a ordem: "))
i=2
j=0
soma=3

while(k>1):
	soma=soma+(4/(i*(i+1)*(i+2))*((-1)**j))
	i=i+2
	j=j+1
while(i<n):
	soma=soma+(4/(i*(i+1)*(i+2))*(-1)**j)
	i=i+2
	j=j+1
	n=n-1
print(round(soma,8))