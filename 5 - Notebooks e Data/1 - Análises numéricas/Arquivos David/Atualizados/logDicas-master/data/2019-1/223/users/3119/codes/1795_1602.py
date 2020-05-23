from numpy import*

x = array(eval(input("Digite o vetor: ")))

i = -1

while(x[i] < max(x)):
	i = i + 1

print(i)	