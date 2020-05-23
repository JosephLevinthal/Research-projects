# Modulo do vetor
from numpy import *
# Entradas
j1 = array(eval(input("Jogadas Eusapia: ")))
j2 = array(eval(input("Jogadas Barsanulfo: ")))
# Variavel
i = 0
s1 = 0
s2 = 0
# Laço
while (i < size(j1)):
	if ((j1[i] == 11 and j2[i] == 33) or (j1[i] == 22 and j2[i] == 11) or (j1[i] == 33 and j2[i] == 22)):
		s1 = s1 + 1
	elif ((j1[i] == 33 and j2[i] == 11) or (j1[i] == 11 and j2[i] == 22) or (j1[i] == 22 and j2[i] == 33)):
		s2 = s2 + 1
	i = i + 1
	
if s1 > s2:
	msg = "EUSAPIA"
elif s2 > s1:
	msg = "BARSANULFO"
else:
	msg = "EMPATE"
	
print(i)
print(msg)
