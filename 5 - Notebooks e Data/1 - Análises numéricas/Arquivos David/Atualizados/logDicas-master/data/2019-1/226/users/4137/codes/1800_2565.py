from numpy import*

med = array(eval(input("medias finais:")))
pre = array(eval(input("horas:")))
hor = array(eval(input("carga horaria:")))

fal = 0
nota = 0
apro = 0

f = zeros(3, dtype=int)

for x in range(size(med)):
	if(med[x] >= 5 and pre[x] >= hor*75/100):
		apro = apro + 1
	elif(pre[x] < hor*75/100):
		fal = fal + 1
	elif(med[x] < 5):
		nota = nota + 1
		
f[0] = apro
f[1] = nota
f[2] = fal


print(f)