from numpy import*

n = array(eval(input("nota: ")))


k = 0
i = 1
soma = 0

while(k < size(n)):
	
	soma = soma + n[k]  * i
	i = i + 1
	k = k + 1
	
print(round(soma / size(n), 2))