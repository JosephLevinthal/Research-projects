from math import*

a = eval(input("angulo: "))                    #angulo
n = int(input("numero de termos da serie: "))  #termos da serie

e = 1  #expoente/fatorial
c = 0  #contador
t = 1  #sinal
x = 0  #somatoria

while (c < n):
	x = x + ( t * ((a ** e) / factorial(e)))
	if t == 1:
		t = -1
	else:
		t = 1
	c = c + 1
	e = e + 2
	
print(round(x, 10))	