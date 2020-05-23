from numpy import*
from numpy.linalg import*

quadro = array([[0,2,11,6,15,11,1],
					[2,0,7,12,4,2,15],
					[11,7,0,11,8,3,13],
					[6,12,11,0,1,2,1],
					[15,4,8,10,0,5,13],
					[11,2,3,2,5,0,14],
					[1,15,13,1,13,14,0]])
c = 0
x = int(input("Cidade 1: "))
y = int(input("Cidade 2: "))
while (y!=-1):
	c = c + quadro[x//111-1, y //111-1] 
	x=y
	y = int(input("Cidade 2: "))
print(c)
		

