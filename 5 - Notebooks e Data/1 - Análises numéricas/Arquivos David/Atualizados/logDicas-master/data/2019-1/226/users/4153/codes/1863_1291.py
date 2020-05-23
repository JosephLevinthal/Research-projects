from numpy import *
from numpy.linalg import *

v = array(eval(input("Insira o vetor: ")))

m = ([[50,60,40],
		[30,40,20],
		[10,15,8]])

r = dot(inv(m),v.T)

print("regular:",round(r[0],0))
print("ortopedico:",round((r[1]),0))
print("infantil:",round((r[2]),0))

mi = min(r)
c = 0
for i in range(size(r)):
	if(r[i] == mi):
		c = i
if(c == 0):
	print("regular")
elif(c == 1):
	print("ortopedico")
elif(c == 2):
	print("infantil")
