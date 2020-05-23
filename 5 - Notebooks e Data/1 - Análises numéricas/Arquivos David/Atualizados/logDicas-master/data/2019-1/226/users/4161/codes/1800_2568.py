n = int(input("base: "))
t = 0
x = n
while t < n:
	v = x*"*" + 2*t*"o" + x*"*" 
	x = x - 1
	print(v)
	t = t + 1