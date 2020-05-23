from numpy import *
v = array(eval(input("notas: ")))
g = array(eval(input("horas: ")))
h = int(input("carga horaria: "))
f = (h/100)*75
r = zeros(3, dtype=int)

for i in range(size(v)):
	if(v[i]<5):
		r[1] = r[1]+1
	elif(g[i]<f):
		r[2] = r[2]+1
	else:
		r[0] = r[0]+1
print(r)