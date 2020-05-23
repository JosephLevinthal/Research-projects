from numpy import *
banho = array(eval(input("digite os tempos do banho: ")))
per = array(eval(input("digite o percentual de abertura da torneira: ")))
i = 0
soma = 0
per = per/100

while(i<size(banho)):
	b = 5*per[i]
	soma = soma + b*banho[i]
	i = i + 1
print(round(soma,2))
	
	