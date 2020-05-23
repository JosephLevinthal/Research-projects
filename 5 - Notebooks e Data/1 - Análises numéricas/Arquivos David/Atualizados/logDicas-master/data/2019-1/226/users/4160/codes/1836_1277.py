from numpy import*
from numpy.linalg import*

x =int(input("Digite o codigo de uma cidade: "))
y= int(input("Digite o codigo de uma cidade: "))

quadro = array([[0,2,11,6,15,11,1],
					[2,0,7,12,4,2,15],
					[11,7,0,11,8,3,13],
					[6,12,11,0,1,2,1],
					[15,4,8,10,0,5,13],
					[11,2,3,2,5,0,14],
					[1,15,13,1,13,14,0]])
a=1
b=0
aux=111
vet =zeros(7,dtype=int)
for i in range(7):
	vet[i] = aux
	aux = aux + 111
for i in range(7):
	if(x==vet[i]):
		a =i
	if(y==vet[i]):
		b=i
print(quadro[a,b])		
	
	