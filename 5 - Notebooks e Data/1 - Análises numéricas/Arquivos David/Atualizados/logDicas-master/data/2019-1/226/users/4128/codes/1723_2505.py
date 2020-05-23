from math import*

x = (eval(input("sen:")))
k = int(input("termos:"))

soma = 0
i = 1
s = 2  
s1 = 0 #termos

while(s1 < k):
	soma = soma + (((x**i)/factorial(i))* (-1)**s)
	s = s + 1
	i = i + 2
	s1 = s1 +1
print(round(soma,10))