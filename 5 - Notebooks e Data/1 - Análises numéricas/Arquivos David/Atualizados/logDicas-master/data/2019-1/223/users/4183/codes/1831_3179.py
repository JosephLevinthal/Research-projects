from numpy import *
v = array(eval(input("Digite: ")))
vf = zeros(size(v),dtype=int)
for i in range(size(v)):
	if(v[i] == 1):
		vf[-1] = 1
		vf[i] = v[i]
print(vf)