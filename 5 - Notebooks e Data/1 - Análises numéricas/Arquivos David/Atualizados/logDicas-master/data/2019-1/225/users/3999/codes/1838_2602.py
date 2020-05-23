from numpy import *
from numpy.linalg import *
nome = ["estafilococo","salmonela","coli"]
M = array([[2 ,1  ,4 ], [1 ,2 , 0 ], [2 ,3  ,2 ]])
v =  array(eval(input("")))
R = dot(inv(M),v.T)
print("estafilococo:",round(R[0],1))
print("salmonela:",round(R[1],1))
print("coli:",round(R[2],1))
mini =0
for i in range(len(R)):
	if(R[mini]>R[i]):
		mini = i
print(nome[mini])