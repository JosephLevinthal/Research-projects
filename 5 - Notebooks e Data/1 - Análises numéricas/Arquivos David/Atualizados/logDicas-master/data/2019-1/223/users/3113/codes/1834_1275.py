from numpy import*
from numpy.linalg import*
m=array(eval(input("")))
#contar as linhas
s=m.shape[1]
#contador
d=0
for i in range(s):
	d=d+m[:,i]
print(d)
	