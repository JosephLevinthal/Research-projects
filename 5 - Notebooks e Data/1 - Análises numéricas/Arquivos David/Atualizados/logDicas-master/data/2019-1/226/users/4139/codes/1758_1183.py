from numpy import*
vetor = array(eval(input("escreva um vetor: ")))

i = 0
nn = 0
while(i<size(vetor)):
	if(vetor[i]>0):
		nn = nn + 1
	i = i + 1
vector = ones(nn, dtype=int)

i2 = 0
i3 = 0
while(i3<size(vector)):
	if(vetor[i2]>0):
		vector[i3] = vetor[i2]
		i3 = i3 + 1
	i2 = i2 + 1

print(vector)