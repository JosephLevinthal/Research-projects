from numpy import *
from numpy.linalg import *
mat = array(eval(input('digite a matriz: ')))
l = mat.shape [0]
c = mat.shape [1]
proc = 0
for i in range(l):
	p = mat[i,:]
	proc = proc + (p[0] * p[1])/2
print(round(proc/l,2))
#batatinha quando nasce
#espalha rama pelo chao
#a menina quando cresce
#poe a mao no coraçao
