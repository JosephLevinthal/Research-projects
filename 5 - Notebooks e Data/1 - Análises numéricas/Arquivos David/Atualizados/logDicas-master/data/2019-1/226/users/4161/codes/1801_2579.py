input("calcule?: ")
h = 1
x = 3
y = 2
while y <= 50:
	h = h + x/y
	y = y + 1
	x = x + 2
print(round(h, 2))