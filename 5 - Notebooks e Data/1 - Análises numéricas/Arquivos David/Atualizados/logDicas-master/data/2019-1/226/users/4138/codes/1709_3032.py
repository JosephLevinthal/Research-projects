x = float(input("insira o valor de x:"))
from math import *
if(x <= 0):
	print(0)
elif(x > 0 and x <= 1):
	print(1)
elif(x > 1 and x <=2):
	print(round(x**(1/2),4))
else:
	print(round(x**(1/3),4))