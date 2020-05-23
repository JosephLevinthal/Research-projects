from numpy import *
j1 = array(eval(input("Primeiro vetor: ")))
j2 = array(eval(input("Segundo vetor: ")))
i = 0
soma1 = 0
soma2 = 0
while (i < size(j1)):
	if (j1[i] == 11 and j2[i] == 33) or (j1[i] == 22 and j2[i] == 11) or (j1[i] == 33 and j2[1] == 22):
		soma1 = soma1 + 1
	elif (j2[i] == 11 and j1[i] == 33) or (j2[i] == 22 and j1[i] == 11) or (j2[i] == 33 and j2[i] == 22):
		soma2 = soma2 + 1
	else:
		msg = "EMPATE"
	i = i + 1
print(size(j1))
if(soma1 > soma2):
	msg = "EUSAPIA"
elif(soma1 < soma2):
	msg = "BARSANULFO"
else:
	msg = "EMPATE"
print(msg)
	