# Ao testar sua solução, não se limite ao caso de exemplo.
y=float(input("eixo de y: "))
x=float(input("eixo de x: "))

if ((y>0)and(x>0)):
	print("Q1")
elif ((y<0)and(x>0)):
	print("Q1")
elif ((y<0)and(x<0)):
	print("Q3")
elif ((y>0)and(x<0)):
	print("Q4")
elif ((y==0)and(x!=0)):
	print ("Eixo de x")
elif ((y!=0)and(x==0)):
	print ("Eixo de y")
elif ((y==0)and(x==0)):
	print ("origem")