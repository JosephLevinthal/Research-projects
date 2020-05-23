from numpy import *
N = int(input("Dimensao da matriz: "))
mg= array(eval(input(": ")))
q = dot(inv(mg),N.T)
for i in range(N):
	for j in range(N):