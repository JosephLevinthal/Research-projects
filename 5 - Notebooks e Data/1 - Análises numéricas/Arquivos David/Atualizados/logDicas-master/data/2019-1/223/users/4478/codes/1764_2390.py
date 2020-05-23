from numpy import*
freq = array(eval(input("frequencia aos meses do ano: ")))
falta = array(eval(input("faltas durante os meses do ano: ")))
i = 0 # posicao do vetor
#mes = 1 #contador de meses
fmax = max(freq)
while(i<size(freq)):
	if(freq[i] == fmax):
		mes = i + 1
	i = i + 1
print(mes)