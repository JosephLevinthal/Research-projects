a = float(input("valor x: "))
b = float(input("valor y: "))

if a > b:
	print("Falta ", round(a-b, 2))
else:
	print("Troco de ", round(b-a, 2))
	