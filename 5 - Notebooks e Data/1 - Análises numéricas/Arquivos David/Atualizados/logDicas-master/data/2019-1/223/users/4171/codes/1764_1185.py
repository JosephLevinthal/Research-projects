from numpy import *

glicose = array(eval(input("nivel de glicose: ")))

i = 0
o = 0
k = 0

while i != size(glicose):
	
	if glicose[i] > 99:
		
		
		o += i
		
		print(o)
		
		k += 1
	
	i += 1
	o = 0

print(k)