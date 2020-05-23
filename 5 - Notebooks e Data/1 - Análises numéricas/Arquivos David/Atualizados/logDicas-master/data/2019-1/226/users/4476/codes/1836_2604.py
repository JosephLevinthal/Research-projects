from numpy import *

m = array(eval(input("dgt: ")))

for i in range(shape(m)[0]):
	print(max(m[i,:]))