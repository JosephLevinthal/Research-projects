from numpy import* 
from numpy.linalg import*
minutos=array(eval(input("minutos: ")))
matriz=array([[10,12,9],[4,4,6],[2,1,1]])
a=minutos.T
cal=dot(inv(matriz),a)


print(cal)

