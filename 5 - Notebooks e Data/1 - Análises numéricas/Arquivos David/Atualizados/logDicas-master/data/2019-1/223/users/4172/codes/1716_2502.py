from math import*
n=int(input("numero natural: "))

tg=sqrt(12)
co=1
sinal=-1
exp=1
a=3
soma=1/(1*((3)**0))
while(n>co):
	soma=soma+(sinal*(1/(a*((3)**exp))))
	exp+=1
	a+=2
	sinal*=-1
	co+=1
soma=soma*tg
print(round(soma,8))
	
