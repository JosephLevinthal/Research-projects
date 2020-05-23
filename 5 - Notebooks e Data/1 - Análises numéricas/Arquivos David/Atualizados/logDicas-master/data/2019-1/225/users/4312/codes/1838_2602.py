from numpy import*
from numpy.linalg import*

consumo = array(eval(input("matriz: ")))
mat = array([[2, 1, 4], [1, 2, 0], [2, 3, 2]])

consumo = consumo.T
					 
r = dot(inv(mat), consumo)

print("estafilococo: ", round(r[0], 1))
print("salmonela: ", round(r[1], 1))
print("coli: ", round(r[2], 1))

if r[0] == min(r):
	print("estafilococo")
elif r[1] == min(r):
	print("salmonela")
else:
	print("coli")
	