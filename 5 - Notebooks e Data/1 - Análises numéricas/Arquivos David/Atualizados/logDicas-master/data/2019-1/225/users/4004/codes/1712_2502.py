n = int(input("numero de termos: "))

c = 0         #contador
e = 0         #expoente
k = 12 ** 0.5 #raiz constante
d = 1         #denominador
s = 1         #sinal
t = 0         #serie de taylor

while c != n:
	t = t + (s * (1/(d * (3 ** e))))  #termo da serie
	if s == 1:
		s = -1
	else:
		s = 1
	c = c + 1
	e = e + 1
	d = d + 2
r = k * t                      #resposta da serie
print(round(r, 8))