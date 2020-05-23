from numpy import *

v = array(eval(input("Medias finais: ")))
f = array(eval(input("Frequencia: ")))
z = zeros(3, dtype=int)

c = int(input("Carga horaria: "))

ap = 0
rp = 0
rf = 0

for i in range(size(v)):
	if (v[i] >= 5 and f[i] >= c*0.75):
		ap = ap + 1
	elif (v[i] < 5):
		rp = rp + 1
	elif (f[i] < c*0.75):
		rf = rf + 1
		
	z [0] = ap
	z [1] = rp
	z [2] = rf
	
print(z)