# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código
from math import*
r = float(input("Insira o raio da esfera: "))
x = float(input("Insira a altura da esfera: "))
num = input("Insira o numero da opcao desejada:(1/2) ")

f = pi * (x ** 2)                  #operacao calota
m = (3 * r) - x
V = (f * m) / 3      
                                                   
w = 4 * pi                         #operacao volume total
v = r ** 3
V2 = (w * v) / 3

q = V2 - V

if(num == "1"):
   print(round(V, 4))
else:
	print(round(q, 4))