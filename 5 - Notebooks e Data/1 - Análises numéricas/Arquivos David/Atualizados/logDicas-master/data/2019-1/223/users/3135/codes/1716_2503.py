n=int(input("Insira a quantidade de termos: "))
pi=0
sinal=-1
while(n>=1):
	if((n%2)==1):
		pi= pi + (4/(2*n-1))
	else:
		pi= pi - (4/(2*n-1))
	n=n-1
		
print(round(pi,8))