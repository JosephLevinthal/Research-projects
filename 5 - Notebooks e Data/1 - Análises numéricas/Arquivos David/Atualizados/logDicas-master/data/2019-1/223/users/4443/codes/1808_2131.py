from math import*
x = eval(input("digite um angulo:"))
N = int(input("numero de termos:"))

cox = 1.0
exp = 2
fato = 2

for i in range(N):
	if(i % 2 == 0 ):
		div = (x**exp)/factorial(fato)
	else:
		div = ((x**exp)/factorial(fato))*(-1)
		cox = cox - div
	exp = exp + 2
	fato = fato + 2
print(round(cox,11))



	