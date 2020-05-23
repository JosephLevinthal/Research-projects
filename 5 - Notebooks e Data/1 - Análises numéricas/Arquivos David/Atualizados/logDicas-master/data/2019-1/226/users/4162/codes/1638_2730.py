# Ao testar sua solução, não se limite ao caso de exemplo.
x= float(input("insira a coordenada do ponto 1: "))
y= float(input("insira a coordenada do ponto 2: "))
a1=x>0
a2=x<0
b1=y>0
b2=y<0
if x>0 and y>0:
	print("Superiores")
if x<0 and y>0:
	print("Superiores")
if x<0 and y<0:
	print("Inferiores")
if x>0 and y<0:
	print("Inferiores")