from numpy import*
from numpy.linalg import*
m=array(eval(input("")))
#contar as linhas
s=m.shape[0]
#contador
d=0
for i in range(s):
	d=max(m[i,:])
	print(d)