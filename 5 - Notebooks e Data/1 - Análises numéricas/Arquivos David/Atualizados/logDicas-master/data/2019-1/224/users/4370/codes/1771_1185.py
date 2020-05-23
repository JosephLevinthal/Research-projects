from numpy import * 
glicose = (eval(input("digite os niveis de glicose: ")))
i = 0
n = 0
while(i < size(glicose)):
	if(glicose[i] > 99):
		print(i)
		n = n + 1
	i = i + 1
print(n)
