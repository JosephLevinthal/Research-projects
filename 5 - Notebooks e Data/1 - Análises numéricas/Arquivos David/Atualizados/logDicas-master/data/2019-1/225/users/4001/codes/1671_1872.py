x = float(input("x: "))
y = float(input("y: "))

if (x == y) and (y == 0):
	print("Origem")
elif (y == 0):
	if (x > 0) or (x < 0):
		print("Eixo X")
elif (x == 0):
	if (y > 0) or (y < 0):
		print("Eixo Y")
elif (y > 0):
	if (x > 0):
		print("Q1")
	else: 
		print("Q2")
elif (y < 0):
	if (x > 0):
		print("Q4")
	else:
		print("Q3")
	
	
