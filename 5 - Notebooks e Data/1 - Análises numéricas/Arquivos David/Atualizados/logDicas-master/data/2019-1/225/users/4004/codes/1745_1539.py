x = float(input("numero real: "))
k = int(input("numero de termos: "))

c = 0   #contador
e = 0   #expoente
S = 0   #Somatoria
s = 1   #sinal


while (c != k):
	S = S + (s * (x ** e))
	c = c + 1
	e = e + 1
	if s == 1:
		s = -1
	elif s == -1:
		s = 1
print(round(S, 7))