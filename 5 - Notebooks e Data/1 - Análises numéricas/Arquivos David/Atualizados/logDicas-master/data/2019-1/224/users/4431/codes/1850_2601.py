from numpy import *
from numpy.linalg import *
x=array([[3,12,1],[12,0,2],[0,2,3]])
y=array([23.6, 52.6, 27.7])
y= y.T
z=solve(x,y)
print("abacate: ",(round(z[0],1)))
print("banana: ",(round(z[1],1)))
print("caqui: ",(round(z[2],1)))
if(z[0]>z[1] and z[0]>z[2]):
	print("abacate")
elif(z[1]>z[0] and z[1]>z[2]):
	print("banana")
else:
	print("caqui")
