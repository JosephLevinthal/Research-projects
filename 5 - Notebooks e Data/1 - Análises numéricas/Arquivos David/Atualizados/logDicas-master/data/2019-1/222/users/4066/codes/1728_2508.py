n = int(input("Numero de termos: "))

t = 1
termo = 3

while (t < n):
	tg = (4*(-1)**(t+1))/((2*t)*(2*t+1)*(2*t+2))
	termo = termo + tg
	t = t+1
print(round(termo,8))