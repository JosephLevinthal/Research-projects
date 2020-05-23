from numpy import *
from numpy.linalg import *
notas=array(eval(input("digite as notas:")))
n = int(input("digite: "))
ah = notas.shape[1]
s = sum(notas[n,:])
med=s/ah
print(round(med,2))
