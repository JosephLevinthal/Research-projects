from numpy import*

t1 =  array(eval(input("Time 1:")))
t2 =  array(eval(input("Time 2:")))

soma = zeros(3 , dtype=int)
i = 0
j = 0
while(i < size(t1)):
	if t1[j] > t2[j]:
		soma[0] = soma[0]+1
	elif  t1[j] == t2[j]:
		soma[1] = soma[1]+1
	elif  t1[j] < t2[j]:
		soma[2] = soma[2]+1
	i = i + 1
	j = j + 1
print(soma)