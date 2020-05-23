# Ao testar sua solução, não se limite ao caso de exemplo.
x = float(input("valor x: "))
y = float(input("valor y: "))

if(x == 0) and (y == 0):
	print("Origem")
elif x > 0:
	if y > 0:
		print("Q1")
	elif y < 0:
		print("Q4")
	else:
		print("Eixo X")
elif(x<0):
	if y <0:
		print("Q2")
	elif y <0:
		print("Q3")
	else:
		print("Eixo Y")