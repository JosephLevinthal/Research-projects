from numpy import *
from numpy.linalg import *

matriz= array(eval(input("matriz:")))

for i in range(matriz):
	for j in range(matriz):
		a1=


quantidade = array([[2,1,4], [1,2,0], [2,3,2]]) #[[2200, 650, 1800]])


populacao = dot(inv(quantidade),consumo.T)

print("estafilococo: ", round(populacao[0], 1))
print("salmonela: ", round(populacao[1], 1))
print("coli: ", round(populacao[2], 1))

if (populacao[0] == min(populacao)):
	print("estafilococo")
elif (populacao[1] == min(populacao)):
	print("salmonela")
elif(populacao[2] == min(populacao)):
	print("coli")
	
