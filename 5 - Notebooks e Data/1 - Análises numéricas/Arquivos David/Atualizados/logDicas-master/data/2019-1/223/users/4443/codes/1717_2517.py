hi = float(input("Digite a altura, em metros, inicial do objeto: ")) #coleta o dado inicial

t = 0
h = hi - 0.5*(9.8)*t**2
while(h>0):
	print("t =", t)
	print("h =", h)
	t = t+1
	h = hi - 0.5*(9.8)*t**2
	h = round(h, 1)
	