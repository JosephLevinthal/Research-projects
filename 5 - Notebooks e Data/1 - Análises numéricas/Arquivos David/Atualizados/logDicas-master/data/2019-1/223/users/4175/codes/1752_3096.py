x = int(input("digite o lugar colocad: "))
h = 0
d = 0

while x!=0:
	if x == 1:
		h = 20 + h
	if x == 2:
		h = 15 + h
	if x == 3:
		h = 10 + h
	if x > 3 and x < 11:
		h = 4 + h
	d = h 
	x = int(input("digite outro lugar: "))
print(d)