from numpy import *
from numpy.linalg import *

# Nosso sistema aqui tem

matriz_dos_coeficientes = array([[1,-1,0,0],
											[0, 1, -1, 0],
											[0, 0, 1, 0],
											[1, 0, 0, 1]])

# Resolução do sistema AX = B
# onde A = Matriz dos coeficientes, X = Vetor do Fluxo e B = Matriz das incognitas

matriz_das_incognitas = array([50,-120,350,870])

Vetor_do_Fluxo = dot(inv(matriz_dos_coeficientes),matriz_das_incognitas)


z = zeros(4)

for i in range(size(Vetor_do_Fluxo)):
	z[i] = round(Vetor_do_Fluxo[i], 1)
	
print(z)