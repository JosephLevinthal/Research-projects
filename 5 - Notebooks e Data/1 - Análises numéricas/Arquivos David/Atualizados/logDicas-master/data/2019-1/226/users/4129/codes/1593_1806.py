from math import*
n = float(input('numero de pessoas:'))

probabilidade = 1- (factorial(365))/factorial(365-n)* 1/(365**n)
porcentagem = probabilidade*100



print(round(porcentagem, 2))