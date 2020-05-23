# Ao testar sua solução, não se limite ao caso de exemplo.
x=float(input("escolha um valor para x: "))
y=float(input("escolha um valor para x: "))
if(x==0) and(x==y):
	print("Origem")
elif(x==0):
	print("Eixo Y")
elif(y==0):
	print("Eixo X")
elif(x>0) and (y>0):
	print("Q1")
elif(x<0) and (y>0):
	print("Q2")
elif(x<0) and (y<0):
	print("Q3")
elif(x>0) and (y<0):
	print("Q4")