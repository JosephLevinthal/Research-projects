from math import*
x = eval(input("angulo medido em radianos: "))
k = int(input("termo em serie: "))

soma = x    #variavel acumuladora
i = 0       #variavel contador
sinal = - 1
cont = 3
while(i < k-1):
	#soma = soma + sinal**(2*i + 1)/ factorial(2*i+1)
	#soma = soma + sinal**(i+1) * (x**(cont)/ factorial(cont))
	soma = soma + sinal**(i+1) * (x**(cont)/ factorial(cont))
	i = i + 1
	cont = cont + 2
	#sinal = sinal * -sinal
print(round(soma,10))