from numpy import *
from numpy.linalg import *
vet=array(eval(input("digite o vetor: ")))

#Matriz do sistema linear
bacterias=array([[2,1,4],
					  [1,2,0],
					  [2,3,2]])
a=dot(inv(bacterias), vet.T)

#Imprimir o nome de cada tipo de bacteria
print("estafilococo:",round(a[0],1))
print("salmonela:",round(a[1],1))
print("coli:",round(a[2],1))

#Imprimir o nome da bacteria com menor populaçao
if a[0] == min(a):
	print('estafilococo')
elif a[1] == min(a):
	print('salmonela')
else:
	print('coli')



