x = float(input())
k = int(input())

soma= 0
i = 0
s = 1
aux = 1

while(x>s):
	soma = soma + (aux /(1+ x))
	if(aux == 1):
		aux == -1
	else:
		aux =1
	
	i = i + i
	s = s - 1
print(round(soma,7))