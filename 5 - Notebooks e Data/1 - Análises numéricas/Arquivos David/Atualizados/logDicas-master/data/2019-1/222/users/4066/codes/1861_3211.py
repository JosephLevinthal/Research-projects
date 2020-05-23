from numpy import *
from numpy.linalg import *

matriz = array([[1, 2, 0.5, 1.5],
					[1.5, 1, 0.5, 1],
					[1, 1, 1, 2.5],
					[2.5, 0.5, 2, 0.5]])

calorias = array(eval(input("Calorias: ")))

gastos = dot(inv(matriz), calorias)

for i in range(size(gastos)):
	if gastos[i] == max(gastos):
		im = i
if im == 0:
	a = 'caminhada'
elif im == 1:
	a = 'corrida'
elif im == 2:
	a = 'bicicleta'
elif im == 3:
	a = 'natacao'
	
print("caminhada:", round(gastos[0], 0))
print("corrida:", round(gastos[1], 0))
print("bicicleta:", round(gastos[2], 0))
print("natacao:", round(gastos[3], 0))
print(a)
