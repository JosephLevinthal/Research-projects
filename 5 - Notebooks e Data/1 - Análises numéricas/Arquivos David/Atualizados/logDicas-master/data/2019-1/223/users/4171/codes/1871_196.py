from numpy import *
from numpy.linalg import *

M = array(eval(input("")))

i = int(input(""))
j = int(input(""))

m = shape(M)[0]
n = shape(M)[1]

for x in range(m):
	for y in range(n):
		if M[x,y] == 'B' and (i,j) == (x,y):
			print("BOMBA")
		if M[x,y] == "L" and (i,j) == (x,y):
			print("LIVRE")
