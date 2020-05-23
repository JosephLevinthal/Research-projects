from numpy import *
from numpy.linalg import *

alimento = array(eval(input("Quantidade: ")))
qtd = array([[2,1,4], [1,2,0], [2,3,2]])

num = dot(inv(qtd),alimento.T)

print("estafilococo: ", round((num[0]), 1))
print("salmonela: ", round((num[1]), 1))
print("coli: ", round((num[2]), 1))

if(num[0] == min(num)):
	print("estafilococo")
elif(num[1] == min(num)):
	print("salmonela")
else:
	print("coli")