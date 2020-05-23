from numpy.linalg import*
from numpy import*
from math import*
matriz=array([[10,12,15],[6,8,12],[12,12,18]])
entrada=array(eval(input()))
aux=[entrada[0]*60,entrada[1]*60,entrada[2]*60]
trans=entrada.T
cal=dot(inv(matriz),aux)
ma=max(cal)
total=size(cal)
print("cadeira:",  round(cal[0], 0))
print("bau:", round(cal[1], 0))
print("mesa:", round(cal[2], 0))
print(total)
for i in total:
	if (cal[i]==ma):
		print("cadeira")
	elif (cal[i]==ma):
		print("bau")
	elif (cal[i]==ma):
		print("mesa")
		