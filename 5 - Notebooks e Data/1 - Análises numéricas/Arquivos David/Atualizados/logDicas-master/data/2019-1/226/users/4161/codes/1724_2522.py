n = int(input("serie: "))
t = n
pi = 1.5
while 0<t:
	a = 1 + (2*t)
	pi = 1 + (t/a)*pi
	t = t - 1
print(round(pi*2, 10))