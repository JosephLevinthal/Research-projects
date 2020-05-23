from numpy import*
from numpy.linalg import*
VC = array(eval(input("digite um vetor [X, Y, Z]: ")))
M = ([[2, 1, 4],[1, 2, 0],[2, 3, 2]])
QUANT = dot(inv(M),VC.T)     # VC = VC
print("estafilococo: ", round(QUANT[0], 1))
print("salmonela: ", round(QUANT[1], 1))
print("coli: ", round(QUANT[2], 1))
if QUANT[0] == min(QUANT):
	print("estafilococo")
elif QUANT[1] == min(QUANT):
	print("salmonela")
else:
	print("coli")