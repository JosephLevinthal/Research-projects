from numpy import*

vetor = array(eval(input("Informe os valores: ")))

posicao = 0
posicaoX = 0

while(posicao < size(vetor)):
	if(vetor[posicao] > 0):
		posicaoX  =  posicaoX  + 1
	posicao = posicao + 1

nvet = zeros(posicaoX , dtype=int)

i = 0
i2 = 0

while(i < size(vetor)):
	if(vetor[i] > 0):
		nvet[i2] = vetor[i]
		i2 = i2 + 1
	i = i+ 1
	
print(nvet)