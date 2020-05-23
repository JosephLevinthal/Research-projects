h = float(input("Altura: "))

t = 0
g = 9.8
h = 100

while(h > 0):
	h = h
	h =  h - ((1/2)*g*t**2)
	t = t + 1
	print(t)
	print(h)