from numpy import*

x = array(eval(input("Glicose:")))

i = 0
soma = 0

while(i < size(x)):
	if(x[i]>99):
		print(i)
		soma = soma + 1
	i = i + 1

print(soma)