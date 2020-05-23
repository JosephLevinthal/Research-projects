tj=float(input("taxa de juros :"))
vp=int(input("valor do apartamento :"))

from math import *
t= 36
Qo=1500

Qf= Qo * (1 + tj) ** t

if (vp <= Qf) :
	print(round(Qf, 2))
	print("Sim")
	
else :
	print(round(Qf,2))
	print("Nao")