from numpy import *
from numpy.linalg import *
bact= array(eval(input("Digite a matriz bacteria: ")))
bact=bact.T
#matriz alimentos
alim=array([[2,1,4],[1,2,0],[2,3,2]])

#Matriz cte
qtd=dot(inv(alim),bact)

print("estafilococo: ",round(qtd[0],1))
print("salmonela: ",round(qtd[1],1))
print("coli: ",round(qtd[2],1))

if(qtd[0] == min(qtd)):
	print("estafilococo")
elif(qtd[1] == min(qtd)):
	print("salmonela")
else:
	print("coli")


