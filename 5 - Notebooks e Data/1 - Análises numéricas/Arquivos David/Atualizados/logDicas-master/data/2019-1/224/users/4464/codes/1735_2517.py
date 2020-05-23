PsI = float(input("insira altura inicial: "))
t = 0
g = 9.8
H = PsI - (1*g*t**2/2)

while (H >= 0):
	print("t =",t)
	print("h =",round(H,1))
	t += 1
	H = PsI - (1*g*t**2/2)