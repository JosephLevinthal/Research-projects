# Ao testar sua solução, não se limite ao caso de exemplo.
x = float(input("x:"))
y = float(input("y:"))

if(x == y == 0):
	print("Origem")
elif(x == 0):
	print("Eixo Y")
elif(y == 0):
	print("Eixo X")
elif(x >= 1) and (y >= 1):
	print("Q1")
elif(x <= 1) and (y >= 1):
	print("Q2")
elif(x <= 1) and (y <= 1):
	print("Q3")
elif(x >=1) and (y <= 1):
	print("Q4")
	

	