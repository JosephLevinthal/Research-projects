r= float(input("insira o raio do tanque: "))
al= float(input("insira a altura da coluna de ar: "))
n= int(input("insira a opcao desejada 1 ou 2: "))
from math import *
ve= (4*pi*(r**3))/3
vce= ((pi*(al**2))*(3*r-al))/3
vc= (ve-vce)
if n==1:
	print(round(vce,4))
if n==2:
	print(round(vc,4))