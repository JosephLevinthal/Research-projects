# Entradas
x = float(input("Insira um numero real: "))
k = int(input("Insira a quantidade de termos da serie: "))
# termo geral:
# i = ((-1)**i) * (x ** i + 1)
i = 0
t = 0
while(t < k):
	x = x + ((-1) ** (i -1) * (x ** i))
	i = i + 2
	t = t + 1
print(x)
	