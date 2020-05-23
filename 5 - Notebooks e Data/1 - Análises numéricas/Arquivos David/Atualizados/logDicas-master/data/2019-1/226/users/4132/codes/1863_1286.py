from numpy.linalg import *
from numpy import *
m = array(eval(input("Digite: ")))

m2 = array([[10,20,30],[50,40,10],[30,10,40]])

aux= dot(inv(m2),m.T)
for i in range(3):
	aux[i]=round(aux[i],0)
print("abacate:",aux[0])
print("manga:",aux[1])
print("pera:",aux[2])
if(min(aux)==aux[0]):
	print("abacate")
elif(min(aux)==aux[1]):
	print("manga")
elif(min(aux)==aux[2]):
	print("pera")
