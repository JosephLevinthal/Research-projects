from numpy import *
from numpy.linalg import *

x = array(eval(input("Vetor de alimentos: ")))

m = array([[2,1,4], [1,2,0], [2,3,2]])

k = dot(inv(m), x.T)

print("estafilococo: ", round(k[0], 1))
print("salmonela: ", round(k[1], 1))
print("coli: ", round(k[2], 1))

if(k[0] < k[1] and k[0] < k[2]):
	print("estafilococo")
elif(k[1] < k[0] and k[1] < k[2]):
	print("salmonela")
else:
	print("coli")