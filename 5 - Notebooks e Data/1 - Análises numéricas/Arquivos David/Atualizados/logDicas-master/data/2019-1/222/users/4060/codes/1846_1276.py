#este o programa nao aceita
from  numpy import*
from numpy.linalg import*

horas=array(eval(input("horas: ")))
zeros=zeros(shape(horas)[0], dtype=int)

for j in range(shape(horas)[0]):
	zeros[j]=sum(horas[:,j])
	
for p in range(shape(horas)[0]):
	if (zeros[p]==max(zeros)):
		print(p+1)

# esse o programa aceita
from numpy import *
from numpy.linalg import *
n=array(eval(input("numero: ")))
c=shape(n)[1]
l=shape(n)[0]
z=zeros(7,dtype=int)

for j in range(c):
	z[j]=sum(n[:,j])
		
for p in range(c):
	if z[p]== max(z):
		print(p+1)

