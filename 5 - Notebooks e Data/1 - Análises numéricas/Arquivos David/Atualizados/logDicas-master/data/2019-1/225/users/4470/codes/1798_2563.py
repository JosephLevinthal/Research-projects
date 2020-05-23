from numpy import *
medias = array(eval(input("medias: ")))
while(size(medias) > 1):
	aprovados = 0
	for i in range(size(medias)):
		if(medias[i] >= 5 and medias[i] < 7):
			aprovados = aprovados + 1
	print(aprovados)
	medias = array(eval(input("medias: ")))