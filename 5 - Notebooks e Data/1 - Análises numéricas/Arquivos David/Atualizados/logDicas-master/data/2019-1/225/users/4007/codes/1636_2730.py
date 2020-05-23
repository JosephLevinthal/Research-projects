# Ao testar sua solução, não se limite ao caso de exemplo.
x = float(input("x: "))
y = float(input("y: "))
if (x < 0 and y <= 0 or x >= 0 and y < 0 ):
	print("inferiores")
elif(x > 0 and y > 0 or x <= 0 and y > 0):
	print("superiores")