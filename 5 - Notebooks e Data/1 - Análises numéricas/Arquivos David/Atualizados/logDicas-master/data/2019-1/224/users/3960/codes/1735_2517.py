h0 = float(input("Insira a altura inicial: "))
t = 0	
h = h0 - (0.5 * 9.8*(t**2))

while(h >= 0):
	print("t =",t)
	print("h =",round(h,2))
	t = t + 1
	h = h0 - (0.5 * 9.8*(t**2))