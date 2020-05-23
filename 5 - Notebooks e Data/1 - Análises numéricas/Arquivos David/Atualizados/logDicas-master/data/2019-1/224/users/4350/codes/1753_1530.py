x = int(input("p"))
y = int(input("v"))
px = float(input("pp"))
py = float(input("pv"))
total = x + y
anos = 0
while total<80000:
	x = x*(px/100)
	y = y*(px/100)
	total = total + x + y
	anos = anos+1
print(anos)	
	