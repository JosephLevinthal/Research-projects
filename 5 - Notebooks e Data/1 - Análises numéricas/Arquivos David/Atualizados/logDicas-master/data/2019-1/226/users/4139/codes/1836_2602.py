from numpy import*
from numpy.linalg import *

alimento = array(eval(input("dados x,y,z: ")))
comida = array([[2,1,4],[1,2,0],[2,3,2]])

alime = dot(inv(comida),alimento.T)

print("estafilococo:",round(alime[0],1))
print("salmonela:",round(alime[1],1))
print("coli:",round(alime[2],1))

if alime[0] ==  min(alime):
	print("estafilococo")
if alime[1] ==  min(alime):
	print("salmonela")
if alime[2] ==  min(alime):
	print("coli")