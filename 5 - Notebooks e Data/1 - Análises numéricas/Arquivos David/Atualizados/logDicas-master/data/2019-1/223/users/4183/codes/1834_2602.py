from numpy import *
from numpy.linalg import *
z = array(eval(input("Digite: ")))
bacterias = array([[2,1,4],[1,2,0],[2,3,2]])
c = dot (inv(bacterias) , z.T)
print("estafilococo: ",round(c[0],1))
print("salmonela: ", round(c[1],1))
print("coli: ", round(c[2],1))
if (c[0] == min(c)):
	print("estafilococo")
elif (c[1] == min(c)):
	print("salmonela")
else:
	print("coli")
