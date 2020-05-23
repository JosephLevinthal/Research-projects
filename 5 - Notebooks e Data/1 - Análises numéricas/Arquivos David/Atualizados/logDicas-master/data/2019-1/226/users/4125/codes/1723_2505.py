from math import*

x = eval(input("angulo em radianos: "))
k = int(input("numero de termos da serie: "))
j = 0
i = 0
soma = 0
while(k>0):
	soma = soma + ((-1)**j)*(((x)**((2*i) + 1))/factorial((2*i)+ 1))
	j = j + 1
	i = i + 1
	k = k - 1
	
print(round(soma,10))