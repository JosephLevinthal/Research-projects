from numpy import *
m = array(eval(input("Medias: ")))
p = array(eval(input("Numero de horas: ")))
ch = int(input("Carga horaria: "))
v = zeros(3, dtype = int)
for i in range(size(m)):
	if(m[i] >= 5 and p[i] >= ch * 75/100):
		v[0] = v[0] + 1
	elif(m[i] < 5 and p[i] >= ch * 75/100):
		v[1] = v[1] + 1
	elif(m[i] >= 5 and p[i] < ch * 75/100):
		v[2] = v[2] + 1
print(v)
	 
