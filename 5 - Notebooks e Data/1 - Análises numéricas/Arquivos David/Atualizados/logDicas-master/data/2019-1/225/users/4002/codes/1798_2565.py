from numpy import*
m = array(eval(input("Medias finais: ")))
p = array(eval(input("Horas presentes: ")))
ch = array(eval(input("Carga horaria: ")))

v = zeros(3, dtype=int)
RF = 0
RN = 0
A = 0

for i in range(size(m)):
	if (p[i] < ch * 75/100):
		RF = RF + 1
		v[2] = RF
	elif (p[i] >= ch *75/100):
		if(m[i] < 5):
			RN = RN + 1 
			v[1] = RN
		elif (m[i] >= 5):
			A = A + 1
			v[0] = A
print(v)
			