from numpy import*
from numpy.linalg import*
tec = array(eval(input("Insira os valores recebidos dos fornecedores: ")))
mat = array([
[50, 60, 40], 
[30, 40, 20],
[10, 15, 8]
])

tec = tec.T
x = dot(inv(mat), tec)

print("regular:",round(x[0], 0))
print("ortopedico:",round(x[1], 0))
print("infantil:",round(x[2], 0))

if x[0] == min(x):
	  print("regular")
if x[1] == min(x):
	  print("ortopedico")
if x[2] == min(x):
	  print("infantil")