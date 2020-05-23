# Ao testar sua solução, não se limite ao caso de exemplo.
x = float(input("v de x:"))
y = float(input("v de y:"))

if(x==0)or(y==0):
	if(x==0)and(y>0)or(y<0):
		print("Eixo Y")
	elif(y==0)and(x>0)or(x<0):
		print("Eixo X")
	else:
		print("Origem")
elif(x<0):
	if(y<0):
		print("Q3")
	elif(y>0):
		print("Q2")
elif(x>0):
	if(y<0):
		print("Q4")
	elif(y>0):
		print("Q1")