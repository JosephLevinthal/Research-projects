t=input("escala da temperatura C/F :")
vt=float(input("valor da temperatura :"))

from math import *

C= (5 / 9 ) * (vt - 32)

F= ((9 / 5) * vt) + 32

if (t.upper() == "C") :
	print(round(F, 2))
	
else :
	print(round(C , 2))