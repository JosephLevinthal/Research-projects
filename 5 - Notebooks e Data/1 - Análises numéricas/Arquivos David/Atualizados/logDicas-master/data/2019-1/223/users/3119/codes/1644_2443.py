# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

from math import*

#Entradas
r = float(input("Raio do tanque: "))
x = float(input("Altura da coluna de ar: "))

#Opcoes 

op = int(input("Qual a opcao desejada 1 ou 2? "))
calota = pi * x**2 * (3*r-x)/3

if(op == 1):
	vol = calota
if(op == 2):
	vol = 4 *pi*r**3/3  - calota 
	
print(round(vol,4))	