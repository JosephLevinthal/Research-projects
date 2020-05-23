from numpy import * 
from numpy.linalg import *
vet = array(eval(input("Alimento: ")))
alim = ([2,1,4],[1,2,0],[2,3,2])
num = dot(inv(alim), vet.T)
print("estafilococo: ", round((num[0]),1))
print("salmonela: ", round((num[1]),1))
print("coli: ", round((num[2]),1))
if num[0] == min(num):
    print("estafilococo")
elif num[1] == min(num):
    print("salmonela")
else:
    print("coli")
