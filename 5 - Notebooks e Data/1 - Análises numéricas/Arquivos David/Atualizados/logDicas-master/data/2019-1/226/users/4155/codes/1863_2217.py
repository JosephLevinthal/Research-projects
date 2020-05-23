from numpy import *
from numpy.linalg import*

v = array(eval(input("v: ")))

for i in range(size(v)):
	for j in range(size(v)):
		if i>j:
			print(min(v))