from math import*
x=eval(input("seno:"))
k=int(input("numero de repeticoes:"))
y=0
i=0
sinal=+x
while(i<k):
	y=y+sinal**(2*i+1)/factorial(2*i+1)
	sinal=-sinal
	i=i+1
print(round(y, 10))