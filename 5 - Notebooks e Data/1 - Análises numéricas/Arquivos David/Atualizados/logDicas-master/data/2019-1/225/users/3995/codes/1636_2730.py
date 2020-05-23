# Ao testar sua solução, não se limite ao caso de exemplo.
x=float(input("coordenada x: "))
y=float(input("coordenada y: "))
if(x>0 and y>0):
	print("Superiores")
if(x<0 and y>0):
	print("Superiores")
if(x<0 and y<0):
	print("Inferiores")
if(x>0 and y<0):
	print("Inferiores")