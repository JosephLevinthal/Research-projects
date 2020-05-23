from numpy import *
from numpy.linalg import *

bac = array(['est', 'sal', 'coli'])
bac = bac.T
alimento = ([[2,1,2], [1,2,3], [4,0,2]])

ali = array(eval(input("mg de alimneto: ")))

c = dot(inv(alimento), ali)

print("Estafilococo: ", round(c[0], 1))
print("Salmonela: ", round(c[1], 1))
print("Coli: ", round(c[2], 1))