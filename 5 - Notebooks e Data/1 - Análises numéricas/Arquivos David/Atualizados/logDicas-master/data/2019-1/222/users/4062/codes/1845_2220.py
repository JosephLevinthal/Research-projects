from numpy import *

m= array(eval(input("Pagamentos: ")))
l = shape(m)[0]
c = shape(m)[1]

for i in range(l):
	print(max(m[i, :]))