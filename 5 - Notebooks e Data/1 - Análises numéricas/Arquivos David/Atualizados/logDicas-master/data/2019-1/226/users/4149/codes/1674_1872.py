x=float(input("Entre com o cvalo de x "))
y=float(input("Entre com o cvalo de y "))
 
if(x==0)and(y==0):
	print("Origem")
elif(x==0):
	print("Eixo Y")
elif(y==0):
	print("Eixo X")
	
if(x>0 and y>0):
	print("Q1")
elif(x<0 and y>0):
	print("Q2")
elif(x<0 and y<0):
	print("Q3")
elif(x>0 and y<0):
	print("Q4")