x = int(input(""))
a = "*"
b = "o"

for i in range(x):
	l = a * (x - i)
	o = b * (i * 2)
	print(l + o + l)