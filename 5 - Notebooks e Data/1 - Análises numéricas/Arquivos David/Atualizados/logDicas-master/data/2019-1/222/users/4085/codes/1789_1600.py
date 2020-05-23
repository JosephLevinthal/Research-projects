from numpy import *
custo = array(eval(input("digite os custos dos itens: ")))
i = 0
if (custo[i] > 80):
	custo[i] = custo[i] - 0.15 * custo [i]
else:
	custo[i] = custo[i]
print(sum(custo, 2))