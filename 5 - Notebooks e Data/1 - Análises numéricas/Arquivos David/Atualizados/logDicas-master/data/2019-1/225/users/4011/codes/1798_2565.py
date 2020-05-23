from numpy import*

nt = array(eval(input("Medias: ")))
fq = array(eval(input("Frequencias: ")))
ch = array(eval(input("Carga horaria: ")))*75/100
v = zeros(3, dtype=int)

i = 0
while(i < size(m)):
	if (nt[i] >= 5) and (fq[i] >= ch[i]):
		v[0] = v[0] + 1
	elif (nt < 5):
		v[1] = v[1] + 1
	elif (fq < ch):
		v[2] = v[2] + 1
		
print(v)