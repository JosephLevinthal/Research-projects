from numpy import*
from numpy.linalg import*
n = array(eval(input("x, y, z? ")))
matriz = array([[8,3,1],[5,12,10],[1,3,2]])
cont = shape(matriz)[1]
dia = n.T
final = dot(matriz,dia)
acumuladora = zeros(cont, dtype=int) 
for j in range(acumuladora):
	total[j] = sum(final[:,j])
x = array(total[0],total[1],total[2])
print(x)