from math import factorial
k=int(input("Digite um numero k: "))


t=0
soma=0
while(t<k):
	y=1/factorial(t)
	soma=soma+y
	t=t+1
print(round(soma, 8))