from numpy import*
from numpy.linalg import *

a=array(eval(input()))
a=a.T
b=array([[2,1,4],[1,2,0],[2,3,2]])
preco=dot(inv(b),a)
print("estafilococo:",round(preco[0],1))
print("salmonela:",round(preco[1],1))
print("coli:",round(preco[2],1))
if(preco[0]==min(preco)):
	print("estafilococo")
elif(preco[1]==min(preco)):
	print("salmonela")
else:
	print("coli")