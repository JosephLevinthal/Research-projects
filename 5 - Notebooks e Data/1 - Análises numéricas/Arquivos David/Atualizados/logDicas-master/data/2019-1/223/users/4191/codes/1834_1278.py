from numpy import *
from numpy.linalg import *
a=int(input("Cidade a: "))
b=int(input("Cidade b: "))
matriz=array([[0,2,11,6,15,11,1],
				  [2,0,7,12,4,2,15],
				  [11,7,0,11,8,3,13],
				  [6,12,11,0,10,2,1],
				  [15,4,8,10,0,5,13],
				  [11,2,3,2,5,0,14],
				  [1,15,13,1,13,14,0]])
posicao=0
while(b != -1):
	posicao=posicao+matriz[(a//100-1),(b//100-1)]
	a=b
	b=int(input("Cidade a: "))
print(posicao)	
	