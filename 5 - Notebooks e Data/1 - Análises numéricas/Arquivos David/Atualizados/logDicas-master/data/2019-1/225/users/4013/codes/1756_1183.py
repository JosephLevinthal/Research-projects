from numpy import*
v = array(eval(input("vetor dos inteiros =")))

i = 0
j = 0 
while(i < size(v)):
	if(v[i] > 0):  #separando os valores positivos
		j = j + 1     
	i = i + 1

i = 0
a = zeros(j , dtype=int) #vetor so com os valores positivos
j = 0
while(j < size(a)): 
	if(v[i] >= 0):
		a[j] = v[i]
	else:
		while(v[i] < 0):
			i = i + 1
		a[j] = v[i]
	i = i + 1
	j = j + 1
print(a)