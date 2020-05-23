from numpy import*
from numpy.linalg import*

horas=array(eval(input("horas: ")))
zeros=zeros(shape(horas)[0], dtype=int)

for i in range(shape(horas)[0]):
	zeros[i]=sum(horas[i,:])
	
print(zeros)		