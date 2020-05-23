from numpy import*
from numpy.linalg import*

v= array(eval(input()))
g=array([[50,60,40],[30,40,20],[10,15,8]])
p= dot(inv(g),v.T)
print("regular:",round(p[0],0))
print("ortopedico:",round(p[1],0))
print("infantil:",round(p[2],0))
if(p[0]==min(p)):
	print("regular")
elif(p[1]==min(p)):
	print("ortopedico")
elif(p[2]==min(p)):
	print("infantil")