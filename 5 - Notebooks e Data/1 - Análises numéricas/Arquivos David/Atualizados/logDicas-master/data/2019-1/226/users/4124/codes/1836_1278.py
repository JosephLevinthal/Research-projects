from numpy import*
from numpy.linalg import *
v = array([[0,2,11,6,15,11,1],
		[2,0,7,12,4,2, 15],
		[11,7,0,11,8,3,13],
		[6,12,11,0,10,2,1],
		[15,4,8,10,0,5,13],
		[11,2,3,2,5,0, 14],
		[1,15,13,1,13,14,0]])
i = 0
x = int(input("Cidade: "))
y = int(input("Cidade: "))
c1 = (x//111)-1
c2 = (y//111)-1
soma = 0

while(y != -1):
	soma = soma + v[c1,c2]
	c1 = c2
	y = int(input("Cidade: "))
	c2 = (y//111)-1
	
print(soma)

	