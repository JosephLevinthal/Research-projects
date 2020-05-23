# Ao testar sua solução, não se limite ao caso de exemplo.
X = float(input(" Digite o valor de  X: "))
Y = float(input(" Digite o valor de Y: "))
if(X==0 and Y==0):
	print("Origem")
elif(Y==0):
	print("Eixo X")
elif(X==0):
	print("Eixo Y")
elif(X>0 and Y>0):
	print("Q1")
elif(X<0 and Y>0):
	print("Q2")
elif(X<0 and Y<0):
	print("Q3")
elif(X>0 and Y<0):
	print("Q4")
