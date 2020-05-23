from numpy import*
from numpy.linalg import*
v=array(eval(input("digite o vetor dos alimentos: ")))
x=array([[2,1,4], 
			[1,2,0], 
			[2,3,2]])
r= dot(inv(x),v.T)
print("estafilococo: " , round(r [0],1))
print("salmonela: " , round(r [1],1))
print("coli: " , round(r [2],1))
if (r[0]==min(r)):
	print("estafilococo")
if (r[1]==min(r)):
	print("salmonela")
if (r[2]==min(r)):
	print("coli")