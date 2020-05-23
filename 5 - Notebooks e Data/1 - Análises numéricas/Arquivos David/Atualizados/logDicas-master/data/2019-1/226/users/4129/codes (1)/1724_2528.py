n = int(input("Numero :"))

l = 0
h = 1

while (n > 1):
	n = n/h
	h = h*10
	l = l + 1
	print(h)