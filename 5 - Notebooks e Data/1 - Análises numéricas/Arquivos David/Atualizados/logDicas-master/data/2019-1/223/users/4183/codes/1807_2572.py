from numpy import *
v = array(eval(input("Digite: ")))
impar = 0
for i in range(size(v)):
	if (v[i] % 2 > 0):
		impar = impar + 1
vf = zeros(impar,dtype=int)
impar = 0
for i in range(size(v)):
	if (v[i] % 2 > 0):
		vf[impar] = v[i]
		impar = impar + 1
print(vf)