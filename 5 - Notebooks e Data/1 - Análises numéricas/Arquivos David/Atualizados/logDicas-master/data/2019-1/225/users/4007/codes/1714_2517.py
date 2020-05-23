h0 = float(input("posicao inicial: "))
t = 0
h = 1
while (t < h0):
	h = h0 - (0.5 * 9.8 * t**2)
	if (h > 0):
		print("t =",round(t, 1))
		print("h =",round(h, 1))
	
	t = t + 1

	
	
	
