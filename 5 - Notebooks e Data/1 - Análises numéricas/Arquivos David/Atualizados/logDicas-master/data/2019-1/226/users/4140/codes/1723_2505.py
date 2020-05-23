from math import*
k=eval(input())
serie=int(input())
i=1
resultado=0
while(i<serie):
	soma=((-1)**i)*((k)**(2*i+1))/factorial(2*i+1)
	resultado=resultado+soma
	i=i+1
resultado=resultado+k
print(round(resultado,10))
