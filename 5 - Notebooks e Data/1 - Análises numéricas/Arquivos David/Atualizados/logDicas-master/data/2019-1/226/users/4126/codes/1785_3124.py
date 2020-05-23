from numpy import*
vetor = array(eval(input("medida: ")))

i = 0
med = 1
while(i<size(vetor)):
	med = (med * vetor[i])
	i = i + 1
media = (med)**(1/size(vetor))
print(round(media,2))