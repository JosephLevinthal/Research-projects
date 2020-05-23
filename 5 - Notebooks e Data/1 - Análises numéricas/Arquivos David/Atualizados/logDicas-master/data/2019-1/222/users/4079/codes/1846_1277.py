from numpy import*
from numpy.linalg import*

tab=array ([[0,2,11,6,15,11,1],[2,0,7,12,4,2,15],[11,7,0,11,8,3,13],[6,12,11,0,10,2,1],[15,4,8,10,0,5,13],[11,2,3,2,5,0,14],[1,15,13,1,13,14,0]])

c1= int(input("Digite o numero da 1o cidade: "))
c2=int(input("Digite o numero da 2o cidade: "))

a= int((c1/111)-1)
b=int((c2/111)-1)

x=tab[a,b]

print(x)