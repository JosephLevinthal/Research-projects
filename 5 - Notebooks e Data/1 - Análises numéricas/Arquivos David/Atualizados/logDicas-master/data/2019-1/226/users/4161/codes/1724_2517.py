h0 = float(input("altura: "))
g = 9.8
t = 0
h = h0
if h>=0:
	while not(h<=0):
		h = h0 - (1/2)*g*(t**2)
		if h>=0:
			print("t =", t)
			t = t + 1
			print("h =",round(h, 1))
			
			
			
			
			
			