a = input("c ou f")
b = float(input("temp"))
if a is "C":
	x = (b*9/5)+32
	print(round(x, 2))
if a is "F":
	y = 5/9*(b-32)
	print(round(y, 2))