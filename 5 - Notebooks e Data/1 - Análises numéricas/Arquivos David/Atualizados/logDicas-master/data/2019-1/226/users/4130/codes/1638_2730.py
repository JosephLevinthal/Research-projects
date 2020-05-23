# Ao testar sua solução, não se limite ao caso de exemplo.
x = float(input("Insira a coordenada x: "))
y = float(input("Insira a coordenada y: "))

if(x > 0 and y > 0):
	print("Superiores")
if(x < 0 and y > 0):
	print("Superiores")
if(x > 0 and y < 0):
	print("Inferiores")
if(x < 0 and y < 0):
	print("Inferiores")