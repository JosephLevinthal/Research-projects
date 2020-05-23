x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if(x> 0 and y > 0):
	print("Q1")
elif(x < 0 and y > 0):
	print("Q2")
elif(x > 0 and y < 0):
	print("Q4")
elif(x == 0 and y > 0):
	print("Eixo Y")
elif(x == 0 and y < 0):
	print("Eixo Y")
elif(x > 0 and y == 0):
	print("Eixo X")
elif(x < 0 and y == 0):
	print("Eixo X")
elif(x == 0 and y == 0):
	print("Origem")
else:
	print("Q3")