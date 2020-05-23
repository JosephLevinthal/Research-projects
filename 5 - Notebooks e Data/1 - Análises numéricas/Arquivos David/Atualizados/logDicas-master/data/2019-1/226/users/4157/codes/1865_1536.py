x = float(input("x:"))
k = int(input("k:"))
a = 0
b = 0
s = x-(x**k)/k
while(x > -1 and x <= 1):
	a = a + 1
	k = k + a
	b = b + 1
	x = x + b
print(round(s, 10))
	
	
	
	