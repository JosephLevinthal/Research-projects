from math import*
from numpy.linalg import*
from numpy import*
m = array([[2,1,4],
			  [1,2,0],
			  [2,3,2]])
x = array(eval(input("digite a matriz: ")))
y = dot(inv(m),x.T)
print("estafilococo:", round(y[0],1))
print("salmonela:", round(y[1],1))
print("coli:", round(y[2],1))
if(y[0]==min(y)):
	print("estafilococo")
elif(y[1]==min(y)):
	print("salmonela")
elif(y[2]==min(y)):
	print("coli")