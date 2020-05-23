from numpy import *

v1 = array(eval(input('Medias finais: ')))
v2 = array(eval(input('Numero de horas: ')))
a = int(input('Carga horaria: '))
v3 = zeros(3, dtype=int)

for i in range(size(v1)):
	if (v1[i] >= 5 and v2[i] >= (a*(75/100))):
		v3[0] = v3[0]+1
	if (v1[i] < 5):
		v3[1] = v3[1]+1
	if (v2[i] < (a*(75/100))):
		v3[2] = v3[2]+1
print(v3)