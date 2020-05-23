from numpy import *
from numpy.linalg import *

ali = array(eval(input("manda: ")))
ali = ali.T

comid = array([[2, 1, 4],[1, 2, 0],[2, 3, 2]])

aliment = dot(inv(comid), ali.T)
				  
print("estafilococo: ", round(aliment[0], 1))
print("salmonela: ", round(aliment[1], 1))
print("coli: ", round(aliment[2], 1))
				  
if(aliment[0] == min(aliment)):
	print("estafilococo")
elif(aliment[1] == min(aliment)):
	print("salmonela")
else:
	print("coli")