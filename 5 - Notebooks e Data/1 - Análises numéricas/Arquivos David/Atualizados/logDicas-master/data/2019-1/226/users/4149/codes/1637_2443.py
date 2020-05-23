from math import *
raio=float(input("entre com o valor do raio: "))
alt=float(input("entre com o valor da altura: "))
num=(input("valor da gasosa ou do ar: (1/2)"))
voles=(4*pi*(raio**3))/3
valcal=((pi*(alt**2)*(3*raio-alt)))/3

if(num=="2"):
	
	print(round(voles-valcal,4))
	
else:
	
	print(round(valcal,4))
	
	
	
	
	
