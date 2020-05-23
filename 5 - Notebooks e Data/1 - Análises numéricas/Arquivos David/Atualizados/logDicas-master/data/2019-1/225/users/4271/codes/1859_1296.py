from numpy import *
from numpy.linalg import *
carros = ([[8, 10, 16], [2,3,5], [1, 2, 3]])
quant = array(eval(input("m: ")))
quant = quant.T
solucao = dot(carros, quant)
print("centurion: ", round(quant[0], 0))
print("tribune: ", round(quant[1], 0))
print("senator: ", round(quant[2], 0))
if quant[0] == min(quant):
	print(centurion)
elif quant[1] == min(quant):
	print(tribune)
else:
	print(senator)