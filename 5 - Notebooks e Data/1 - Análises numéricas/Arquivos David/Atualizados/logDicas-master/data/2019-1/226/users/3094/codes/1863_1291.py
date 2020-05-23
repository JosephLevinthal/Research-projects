from numpy import *
from numpy.linalg import *

mat = array([[50,60,40],
				 [30,40,20],
				 [10,15,8]])
mp = array(eval(input("x,y,z: ")))


c = dot(inv(mat),mp.T)
print("regular:", round(c[0],0))
print("ortopedico: ", round(c[1],0))	
print("infantil: ", round(c[2],0))	

if c[0]==min(c):
	print("regular")
elif c[1]==min(c):
	print("ortopedico")
else:
	print("infantil")