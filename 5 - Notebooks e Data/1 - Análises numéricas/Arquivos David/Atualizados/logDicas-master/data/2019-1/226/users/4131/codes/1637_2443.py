from math import *
r= float(input("raio:"))
x= float(input("altura:"))
opcao= int(input("numero 1 ou 2:"))
esfera= ( 4* pi *r**3)/3
calota= ( pi * x**2 *(3*r-x))/3
comb= esfera-calota
ar=calota
if(opcao==1):
	print(round(ar,4))
else:
	print(round(comb,4))