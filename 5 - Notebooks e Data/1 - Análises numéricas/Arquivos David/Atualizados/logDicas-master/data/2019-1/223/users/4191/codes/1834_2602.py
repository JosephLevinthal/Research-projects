from numpy import *
from numpy.linalg import *

vet=array(eval(input("X,Y,Z: ")))

matriz=array([[2,1,4],[1,2,0],[2,3,2]])
XYZ=dot(inv(matriz), matriz.T)
print("estafilococo:", round(XYZ[0],1))
print("salmonela:", round(XYZ[1],1))
print("coli:", round(XYZ[2],1))

if(XYZ[0]==min(XYZ)):
	print("estafilococo")
elif(XYZ[1]==min(XYZ)):
	print("salmonela")
elif(XYZ[2]==min(XYZ)):
	print("coli")