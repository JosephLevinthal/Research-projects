from numpy import *
gols = array(eval(input("gols marcados: ")))
gols2 = array(eval(input("gols marcados pelo adversario: ")))
resultado = gols-gols2
v = 0
d = 0
e = 0
for i in resultado:
	if(i == 0):
		e = e + 1
	elif(i > 0):
		v = v + 1
	else:
		d = d + 1
z = zeros(3,dtype = int)
z[0] = v
z[1] = e
z[2] = d
print(z)
