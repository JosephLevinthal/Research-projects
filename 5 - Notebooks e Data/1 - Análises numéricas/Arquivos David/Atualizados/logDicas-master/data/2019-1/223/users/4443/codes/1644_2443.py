from math import *

# Leitura dos dados
r = float(input("raio do tanque: "))
x = float(input("altura da coluna de ar: "))
w = int(input("digite a opcao desejada: "))

#Calculo dos volumes
Ve = (4 * pi * r**3)/3

a = pi * x**2
b = (3*r) - x
Vce = (a * b)/3

gas = Ve - Vce
ar = Vce

if(w == 1):
	print(round(ar, 4))

if(w == 2):
	print(round(gas, 4))

