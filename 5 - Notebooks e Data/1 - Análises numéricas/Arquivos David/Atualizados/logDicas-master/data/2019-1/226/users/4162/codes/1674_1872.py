# Ao testar sua solução, não se limite ao caso de exemplo.
x= float(input("insira a coordenada x: "))
y= float(input("insira a coordenada y: "))
if (x>0) and (y>0):
	print("Q1")
elif (x<0)and(y>0):
	print("Q2")
elif (x<0)and(y<0):
	print("Q3")
elif (x>0)and(y<0):
	print("Q4")
elif ((x>0)or(x<0))and(y==0):
	print("Eixo X")
elif (x==0)and((y>0)or(y<0)):
	print("Eixo Y")
elif (x==0)and(y==0):
	print("Origem")