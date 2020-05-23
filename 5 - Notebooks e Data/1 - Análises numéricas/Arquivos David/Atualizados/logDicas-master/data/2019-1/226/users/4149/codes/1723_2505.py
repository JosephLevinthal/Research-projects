
from math import*
x=eval(input("Entre com o valor do angulo: "))
n=int(input("entre com os termos da serie: "))
soma=0
i=1
j=n-1

while(j>i):
	tg=x**(2*i+1)
	tg1=(factorial(2*i+1))
	soma=soma+(((-1)**i) * (tg))/tg1
	i=i+1
					  
print(round(soma,10))
		  