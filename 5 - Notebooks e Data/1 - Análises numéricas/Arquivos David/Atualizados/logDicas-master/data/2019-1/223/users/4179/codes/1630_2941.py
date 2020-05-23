import math
Vi=float(int(input("Qual o valor inicial investido: ?")))
j=float(input("Qual a taxa de juros do investimento: ?"))
n=float(int(input("Qual o numero de meses do investimento: ?")))

Vf=Vi*(1+j)**n

print(round(Vf,2))