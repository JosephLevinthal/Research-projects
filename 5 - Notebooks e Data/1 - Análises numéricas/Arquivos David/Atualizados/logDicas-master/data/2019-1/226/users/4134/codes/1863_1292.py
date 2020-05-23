from numpy import*
from numpy.linalg import*
n = array(eval(input("Vet:")))
x = array([8,3,1],[5,12,10],[1,3,2])
n = n.T
j = dot(inv(x),a)
print(j)