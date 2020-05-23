from numpy import*

v = array(eval(input("V: ")), dtype=str)
s = size(v) - 1
x = size(v)//2


for i in range(x):
	aux = 0
	aux = v[i]
	v[i] = v[s-i]
	v[s-i] = aux	

print(v)