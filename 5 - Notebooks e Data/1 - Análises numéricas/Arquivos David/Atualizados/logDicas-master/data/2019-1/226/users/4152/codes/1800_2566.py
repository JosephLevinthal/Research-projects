from numpy import *
vet = array(eval(input("Vetor: ")))
vet1 = zeros(6, dtype=float)
seg = 0
ter = 0
qua = 0
qui = 0
sex = 0
sab = 0
for i in range(size(vet)):
	if (vet[i] == 2):
		seg = seg + 1
	elif (vet[i] == 3):
		ter = ter + 1
	elif (vet[i] == 4):
		qua = qua + 1
	elif (vet[i] == 5):
		qui = qui + 1
	elif (vet[i] == 6):
		sex = sex + 1
	elif ( vet[i] == 7):
		sab = sab + 1
perc1 = round((seg * 100) / size(vet), 1)
perc2 = round((ter * 100) / size(vet), 1)
perc3 = round((qua * 100) / size(vet), 1)
perc4 = round((qui * 100) / size(vet), 1)
perc5 = round((sex * 100) / size(vet), 1)
perc6 = round((sab * 100) / size(vet), 1)
vet1[0] = perc1
vet1[1] = perc2
vet1[2] = perc3
vet1[3] = perc4
vet1[4] = perc5
vet1[5] = perc6
print(vet1)