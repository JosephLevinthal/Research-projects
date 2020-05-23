from numpy import *
E = array(eval(input("Jogada 1: ")))
B = array(eval(input("Jogada 2: ")))
i = 0 #posicao do vetor
ve = 0
vb = 0
while (i < size(E)):
	if (E[i] != B[i]):
		if (E[i] == 11) and (B[i] == 33):
			ve = ve + 1
		elif (E[i] == 22) and (B[i] == 11):
			ve = ve + 1
		elif (E[i] == 33) and (B[i] == 22):
			ve = ve + 1
		elif (B[i] == 11) and (E[i] == 33):
			vb = vb + 1
		elif (B[i] == 22) and (E[i] == 11):
			vb = vb + 1
		elif (B[i] == 33) and (E[i] == 22):
			vb = vb + 1
	i = i + 1
if (ve > vb):
	print(i)
	print("EUSAPIA")
elif(ve == vb):
	print(i)
	print("EMPATE")
else:
	print(i)
	print("BARSANULFO")
	