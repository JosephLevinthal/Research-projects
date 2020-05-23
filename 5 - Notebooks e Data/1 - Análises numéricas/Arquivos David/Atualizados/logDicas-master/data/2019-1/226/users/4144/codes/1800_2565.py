from numpy import *
a = array(eval(input("media dos alunos: ")))
b = array(eval(input("presenca em horas: ")))
c = int(input("carga da materia: "))
d = zeros(3, dtype=int)
for i in range(size(a)):
	if(a[i]>=5 and b[i]>=(0.75*c)):
		d[0]= d[0] + 1
	elif(a[i]<5):
		d[1]= d[1] + 1
	elif(b[i]<(0.75*c)):
		d[2]= d[2] + 1
print(d)