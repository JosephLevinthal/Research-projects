from numpy import *
a = array(eval(input("Notas finais: ")))

R = 0
for i in range(size(a)):
	if (a[i] >= 5):
		R = R
	elif (a[i] < 5):
		R = R + 1	
v = zeros(R, dtype=int)
vs = 0
for i in range(size(a)):
	if (a[i] < 5):
		v[vs] = i
		vs = vs + 1

print(R)
print(v)