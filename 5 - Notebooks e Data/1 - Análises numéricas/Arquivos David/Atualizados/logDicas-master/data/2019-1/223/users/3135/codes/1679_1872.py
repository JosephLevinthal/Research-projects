# Ao testar sua solução, não se limite ao caso de exemplo.
x=float(input("Insira o valor de X:"))
y=float(input("Insira o valor de Y:"))


if(x==0 and y==0):
	print("Origem")
elif(y==0):
	print("Eixo X")
elif(x==0):
	print("Eixo Y")
elif(x>0 and y>0):
	print("Q1")
elif(x<0 and y>0):
	print("Q2")
elif(x<0 and y<0):
	print("Q3")
elif(x>0 and y<0):
	print("Q4")
