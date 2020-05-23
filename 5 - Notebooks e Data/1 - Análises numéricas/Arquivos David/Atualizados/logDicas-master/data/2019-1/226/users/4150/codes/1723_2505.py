from math import*


ang = eval(input("angulo: "))
k = int(input("numero de termos: "))

soma= 0
i=0
fim = k-1

while(i <=fim):
	soma = soma + (-1)**i*((ang**(2*i+1)/factorial(2*i+1)))
	i = i+1
print(round(soma, 10))