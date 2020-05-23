from numpy import *
from numpy.linalg import *

vet = array(eval(input("insira:")))

const = array([[4,5,2],
				  	[3,2,2],
					[2,3,3]])
r = dot(inv(const),vet.T)

print("grande:",round(r[0],0))
print("medio:",round(r[1],0))
print("pequeno:",round(r[2],0))

if(r[0] == max(r)):
	print("grande")
elif(r[1] == max(r)):
	print("medio")
elif(r[2] == max(r)):
	print("pequeno")