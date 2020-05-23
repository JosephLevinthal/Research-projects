from math import*

x = eval(input("digite o x: "))
k = int(input("digite o k: "))
#criar variavel acumuladora e contadora
soma = 0
i = 0
final = k - 1
while(k>i):
	tg = x**(2*i + 1)
	tgd = factorial((2*i)+1)
	soma = soma + (((-1)**i)*tg)/tgd
	i = i + 1
print(round(soma,10))
