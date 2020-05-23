from numpy import*
vet = array(eval(input("vetor de faltas a cada dia:")))

v = zeros(6 , dtype=float)

seg = 0
ter = 0
qua = 0
qui = 0
sex = 0
sab = 0

for i in vet:
	if(i == 2):
		seg = seg + 1
	elif(i == 3):
		ter = ter + 1
	elif(i == 4):
		qua = qua + 1
	elif(i == 5):
		qui = qui + 1
	elif(i == 6):
		sex = sex + 1
	elif(i == 7):
		sab = sab + 1
t = seg + ter + qua + qui + sex + sab
for i in v:
	v[0] = round((seg/t) * 100 , 1)
	v[1] = round((ter/t) * 100 , 1)
	v[2] = round((qua/t) * 100 , 1)
	v[3] = round((qui/t) * 100 , 1)
	v[4] = round((sex/t) * 100 , 1)
	v[5] = round((sab/t) * 100 , 1)
print(v)