from numpy import *

ve = array(eval(input("v1: ")))
vb = array(eval(input("v2: ")))
cont = 0
We = 0
Wb = 0
while cont < size(ve):
	if ve[cont] == 11:
		if vb[cont] == 22:
			Wb = Wb + 1
		elif vb[cont] == 33:
			We = We + 1
	elif ve[cont] == 22:
		if vb[cont]== 33:
			Wb = Wb + 1
		elif vb[cont] == 11:
			We = We + 1
	else:
		if vb[cont]== 11:
			Wb = Wb + 1
		elif vb[cont] == 22:
			We = We + 1
	cont = cont + 1
print(cont)
if We > Wb:
	print("EUSAPIA")
elif We < Wb:
	print("BARSANULFO")
elif We == Wb:
	print("EMPATE")

	