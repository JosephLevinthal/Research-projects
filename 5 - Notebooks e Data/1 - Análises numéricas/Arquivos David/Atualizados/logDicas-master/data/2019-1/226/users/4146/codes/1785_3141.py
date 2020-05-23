from numpy import *
n = array(eval(input("Valores: ")))
i = 0
p = 1
soma = 0

while(i < size(n)):
	soma = soma + (n[i]**(1/6))
	i = i + 1
	
med = (soma**6)/(size(n))**6	
	
print(round(med, 2))
	