# Ao testar sua solução, não se limite ao caso de exemplo.
x=float(input("Digite a coordenada x: "))
y=float(input("Digite a coordenada y: "))

if(x==0 and y==0):
	print("Origem")
elif((x==0 and y>0) or (x==0 and y<0)):
	print("Eixo Y")
elif((y==0 and x>0) or (y==0 and x<0)):
	print("Eixo X")
elif(x>0 and y>0):
	print("Q1")
elif(x<0 and y>0):
	print("Q2")
elif(x<0 and y<0):
	print("Q3")
elif(x>0 and y<0):
	print("Q4")

		