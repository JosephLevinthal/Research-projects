from numpy import*
a = array(eval(input("jogadores de eusapia")))
b = array(eval(input("jogadores de barsanulfo")))
i = 0 #posicao do vetor
j = 0 #vitorias eusapia
k = 0 #vitorias barsanulfo
while(i < size(a)):
	if(a[i]==11 and b[i]==22):
		k = k +1
	elif(a[i]==11 and b[i]==33):
		j = j +1
	elif(a[i]==22 and b[i]==11):
		j = j + 1
	elif(a[i]==22 and b[i]==33):
		k = k + 1
	elif(a[i]==33 and b[i]==11):
		k = k + 1
	elif(a[i]==33 and b[i]==22):
		j = j + 1
	i = i + 1
print(i)
if(j>k):
	print("EUSAPIA")
elif(j<k):
	print("BARSANULFO")
else :
	print("EMPATE")

	
