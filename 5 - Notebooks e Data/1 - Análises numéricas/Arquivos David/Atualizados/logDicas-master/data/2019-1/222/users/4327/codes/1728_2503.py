n = int(input("Numero de termos: "))

t = 0
soma = 0

while (t < n):
	tg = (4*(-1)**(t))/(2*t+1)
	soma = soma + tg
	t = t + 1
	
print(round(soma, 8))