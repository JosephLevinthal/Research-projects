# Ao testar sua solução, não se limite ao caso de exemplo.
x = float(input("Coordenada x: "))
y = float(input("Coordenada y: "))
if (x != 0 and y == 0):
	print("Eixo X")
elif(x > 0 and y > 0):
	print("Q1")
elif(x < 0 and y > 0):
	print("Q2")
elif(x < 0 and y < 0):
	print("Q3")
elif(x > 0  and y < 0):
	print("Q4")
elif(x == 0 and y == 0):
	print("Origem")
else:
	print("Eixo Y")