from numpy import*
from numpy.linalg import*

mg = array(eval(input("mg alimento: ")))
mg = mg.T

alimentos = array([[2,1,4], [1,2,0], [2,3,2]])

bacteria = dot(inv(alimentos), mg)

print("estafilococo:", round(bacteria[0], 1))
print("salmonela:", round(bacteria[1], 1))
print("coli:", round(bacteria[2], 1))

if(bacteria[0] == min(bacteria)):
	print("estafilococo")
elif(bacteria[1] == min(bacteria)):
	print("salmonela")
else:
	print("coli")
	