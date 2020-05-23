from numpy import*
from numpy.linalg import*
v = array(eval(input("x y z: ")))
v = v.T
a = array([[10,20,30],[50,40,10],[30,10,40]])
r = dot(inv(a),v.T)
print("abacate:",round(r[0]),)
print("manga:",round(r[1]),)
print("pera:",round(r[2]),)
if(r[0]<r[1] and r[0]<r[2]):
	print("abacate")
elif(r[1]<r[2] and r[1]<r[0]):
	print("manga")
else:
	print("pera")