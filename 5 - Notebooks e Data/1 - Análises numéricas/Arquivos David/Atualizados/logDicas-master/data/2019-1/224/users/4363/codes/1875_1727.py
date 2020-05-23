from numpy import *
from numpy.linalg import *
notas=array(eval(input("digite as notas:")))
a=shape(notas) [0]
b=shape(notas) [1]
vm=zeros(a, dtype=float)
for i in range(a):
		for j in range(b):
			if notas[i,j]==max(notas[i,:]):
				vm[i]=notas[i,j]
maior=max(vm)
print(maior)