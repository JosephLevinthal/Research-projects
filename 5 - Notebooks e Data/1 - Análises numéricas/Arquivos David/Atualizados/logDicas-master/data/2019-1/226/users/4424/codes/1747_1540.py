from math import*
x=eval(input("escreva: "))
k=int(input("escreva: "))

soma=0
i=0
fim=k

while(i<fim):
	soma=soma+(-1)**(i)*((x**i)/(factorial(2*i)))
	i=i+1
	
print(round(soma, 6))