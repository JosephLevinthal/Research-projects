from numpy import *
from numpy.linalg import *

x = array(eval(input()))
y = array([[2,1,4],[1,2,0],[2,3,2]])

a = dot(inv(y),x.T)
print("estafilococo: ",round(a[0],1))
print("salmonela: ",round(a[1],1))
print("coli: ",round(a[2],1))

if a[0] == min(a):
	print("estafilococo")
elif a[1] == min(a):
	print("salmonela")
else:
	print("coli")