from numpy.linalg import*
from numpy import *

vetor1=array(eval(input("")))

vetor2=array([[2,1,4],[1,2,0],[2,3,2]])

w=dot(inv(vetor2),vetor1.T)

print("estafilococo:" ,round(w[0],1))
print("salmonela:" ,round(w[1],1))
print("coli:" ,round(w[2],1))

if w[0]==min(w):
	print("estafilococo")
elif w[1]==min(w):
	print("salmonela")
elif w[2]==min(w):
	print('coli')