# Ao testar sua solução, não se limite ao caso de exemplo.
x = float(input("Digite aqui a coordenada x: "))
y = float(input("Digite aqui a coordenada y: "))
if ((x != 0) and (y != 0)):
	if ((x > 0) and (y > 0)):
		msg = "Q1"
	elif ((x < 0) and (y < 0)):
		msg = "Q3"
	elif ((x > 0) and (y < 0)):
		msg = "Q4"
	else:
	   msg = "Q2"
elif (((x == 0) and (y != 0)) or ((y == 0) and (x != 0))):
	if (x == 0):
		msg = "Eixo Y"
	else:
		msg = "Eixo X"
else:
		msg = "Origem"
print(msg)