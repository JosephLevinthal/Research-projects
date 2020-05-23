from math import *
a = float(input('valor de x: '))
if a <= 0:
	print(0)
elif ((a>0) and (a<1)) or (a == 1):
	print(1)
elif ((a>1) and (a<2)) or (a == 2):
	print(round(sqrt(a),4))
elif (a>2):
	print(round(a**(1/3),4))