# Ao testar sua solução, não se limite ao caso de exemplo.
x = float(input("valor de x: "))
y = float(input("valor de y: "))

if(x > 0) and (y > 0):
	print("Q1")
elif(x < 0) and (y > 0):
	print("Q2")
elif(x < 0) and (y < 0):
	print("Q3")
elif(x > 0) and (y < 0):
	print("Q4")
else:
	if(x > 0) or (x < 0):
		print("Eixo X")
	elif( y > 0) or (y <0): 
		print("Eixo Y")
	else: 
		if(x == 0) and (y == 0): 
			print("Origem")
		else: 
			print("nao existe")