from numpy import*
gl = array(eval(input("indice glicemico: ")))
i = 0 #posicao do vetor
oc = 0 #numero de ocorrencias

while(i<size(gl)):
	if(gl[i]>99):
		print(i)
		oc = oc + 1
	i=i+1
print(oc)
	