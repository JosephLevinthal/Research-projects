from numpy import *
from numpy.linalg import *
quant = ([[2, 1, 4], [1, 2, 0], [2, 3, 2]])
n = array([2200, z, ","])
n = n.T
quant = dot(inv(quant), n)
print("estafilococo: ", round(quant[0], 1))
print("salmonela: ", round(quant[1], 1))
print("coli: ", round(quant[2], 1))
if quant[0] == min(quant):
	print("estafilococo")
elif quant[1] == min(quant):
	print("salmonela")
else:
	print("coli")