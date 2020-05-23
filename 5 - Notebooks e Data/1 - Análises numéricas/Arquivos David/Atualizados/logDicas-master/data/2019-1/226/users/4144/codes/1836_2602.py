from numpy import *
from numpy.linalg import*
v = array(eval(input("digite a qtd de alimento: ")))
v = v.T
comida = array([[2,1,4],[1,2,0],[2,3,2]])
r = dot(inv(comida),v.T)
print("estafilococo:", round(r[0],1))
print("salmonela:", round(r[1],1))
print("coli:", round(r[2],1))
if(r[0]==min(r)):
	print("estafilococo")
elif(r[1]==min(r)):
	  print("salmonela")
elif(r[2]==min(r)):
	  print("coli")