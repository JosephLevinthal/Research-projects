from math import*
x=eval(input("Insira o angulo de X em radiano: "))
k= int(input("Insira o valor de K termos da serie: "))

cont=1
sinal=-1
soma=x
exp=3

while (cont<k):
	soma=soma+(sinal*(x**exp)/factorial(exp))
	sinal= sinal*-1
	exp=exp+2
	cont+=1
print(round(soma,10))