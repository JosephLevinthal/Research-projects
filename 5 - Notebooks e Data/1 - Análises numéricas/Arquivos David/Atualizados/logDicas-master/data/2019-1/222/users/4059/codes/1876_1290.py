from numpy import *
from numpy.linalg import *

tempo=array([[10,12,15],[6,8,12],[12,12,18]])
vet=array(eval(input()))
quantidade=dot(inv(tempo),vet.T)
q=quantidade*60

print("cadeira: ", round(q[0],0))
print("bau: ", round(q[1],0))
print("mesa: ", round(q[2],0))
if (q[0]==max(q)):
	print("cadeira")
if (q[1]==max(q)):
	print("bau")
if (q[2]==max(q)):
	print("mesa")