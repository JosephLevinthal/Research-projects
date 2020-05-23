from numpy import *
from numpy.linalg import *
a = array(eval(input("digite: ")))
alim=array([[2,1,4],[1,2,0],[2,3,2]])
XYZ=dot(inv(alim),a.T)
print("estafilococo:",round(XYZ[0],1))
print("salmonela:",round(XYZ[1],1))
print("coli:",round(XYZ[2],1))
if(XYZ[0]==min(XYZ)):
	print("estafilococo")
elif(XYZ[1]==min(XYZ)):
	print("salmonela")
else:
	print("coli")