from numpy import*

vet = array(eval(input("Dias em que faltou: ")))
final = zeros(6, dtype=float)
seg = 0
ter = 0
qua = 0
qui = 0
sex = 0
sab = 0

for x in range(size(vet)):
	if (vet[x] == 2):
		seg = seg + 1
	elif(vet[x] == 3):
		ter = ter + 1
	elif(vet[x] == 4):
		qua = qua + 1
	elif(vet[x] == 5):
		qui = qui + 1
	elif(vet[x] == 6):
		sex = sex + 1
	elif(vet[x] == 7):
		sab = sab + 1


a = round((seg * 100)/size(vet), 1)
b = round((ter * 100)/size(vet), 1)
c = round((qua * 100)/size(vet), 1)
d = round((qui * 100)/size(vet), 1)
e = round((sex * 100)/size(vet), 1)
f = round((sab * 100)/size(vet), 1)

final[0] = a
final[1] = b
final[2] = c
final[3] = d
final[4] = e
final[5] = f
print(final)
