h = float(input("altura: "))
g = 9.8
t = 0
H = h - (1/2)*g*(t**2)
while(H > 0):
	print(t)
	print(round(H,1))
	H = h - (1/2)*g*(t**2)
	t = t + 1
	