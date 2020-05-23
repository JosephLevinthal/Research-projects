from numpy import*
a = array(eval(input("vetor 1")))
i= 0 #quantidade de elementos nao negativos
j= 0 #copiar os elementos nao negativos do vetor de entrada para o vetor de saida
k= 0 # posicao do vetor entrada
l= 0 # posicao do vetor saida
while (k < size(a)) :
	if (a[k] > 0):
		i = i + 1
	k = k + 1
k=0
b = arange(i)
while (k < size(a)):
	if (a[k] > 0):
		b[j]=a[k]
		j= j + 1
	k = k + 1
print(b)
		