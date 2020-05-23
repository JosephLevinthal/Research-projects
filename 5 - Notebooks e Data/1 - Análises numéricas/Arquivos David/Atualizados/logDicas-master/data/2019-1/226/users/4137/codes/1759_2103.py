from numpy import*

a = array(eval(input("Vetor A:")))
b = array(eval(input("Vetor B:")))

i = 0
j = -1
d = 0
x = zeros(size(b) , dtype=int)
while(i < size(a)):
	x[i] = b[j]
	i = i + 1
	j = j-1

i = 0
while(i < size(a)):
	if(x[i] >= b[i]):
		print(x[i])
	else:
		print(a[i])
	i = i + 1
	