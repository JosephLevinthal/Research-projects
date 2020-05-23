from numpy import*
from numpy.linalg import*

bact = array([[2, 1, 4], [1,2,0], [2,3,2]])
alim = array(eval(input("alimentos: ")))
alim = alim.T

x = dot(inv(bact), alim)
print("estafilococo: ", round(x[0], 1))
print("salmonela: ", round(x[1], 1))
print("coli: ", round(x[2], 1))

if(x[0] == min(x)):
	print("estafilococo")
elif(x[1] == min(x)):
	print("salmonela")
else:
	print("coli")