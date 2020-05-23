from numpy import *
v = array(eval(input("Digite: ")))
d = 0
for i in range(size(v)):
	if (v[i] < (size(v)*70)//100):
		d = d + 1
print(d)
do = 0
for i in range(size(v)):
	if(v[i] < (size(v)*70)//100):
		d = v[i]
	
print(v)