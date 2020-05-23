h0 = float(input())

t = 0
h = h0 - (1/2) * 9.8 * (t ** 2)

while(h > 0):
	print("t = ", t)
	print("h = ", round(h, 1))
	
	t = t + 1
	h = h0 - (1/2) * 9.8 * (t ** 2)