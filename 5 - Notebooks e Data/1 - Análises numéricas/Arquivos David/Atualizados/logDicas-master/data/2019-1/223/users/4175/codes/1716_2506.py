x = float(input("x: "))
y = float(input("y: "))
w = float(input("w: "))
t = 0
y = y/100

while 0<x<12000:
	a = x*y
	x = a + x
	x = x - w
	t += 1 
if x <= 0:
	print("EXTINCAO")
else:
	print("LIMITE")

print(t)