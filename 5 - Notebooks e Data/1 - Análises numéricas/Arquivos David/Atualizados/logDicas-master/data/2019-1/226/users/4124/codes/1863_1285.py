from numpy import *
from numpy.linalg import *
mat = array(eval(input("Vetor: ")))
x = array([[4,5,2],[3,2,2],[2,3,3]])
total = dot(inv(x),mat.T)
print("grande: ",round(total[0],0))
print("medio: ",round(total[1],0))
print("pequeno: ",round(total[2],0))
if max(total) == total[0]:
	print("grande")
elif max(total) == total[1]:
	print("medio")
else:
	print("pequeno")
