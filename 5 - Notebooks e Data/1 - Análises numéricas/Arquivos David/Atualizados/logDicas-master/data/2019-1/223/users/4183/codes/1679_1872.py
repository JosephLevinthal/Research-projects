# Ao testar sua solução, não se limite ao caso de exemplo.
x = float(input("Valor de x: "))
y = float(input("Valor de y: "))
if (x == 0 and y == 0):
	print("Origem")
elif (y == 0):
	print("Eixo X")
elif (x > 0 and y > 0):
	print("Q1")
elif (x < 0 and y < 0):
	print("Q3")
elif (x < 0 and y > 0):
	print("Q2")
elif (x > 0 and y < 0):
	print("Q4")
else:
	print("Eixo Y")