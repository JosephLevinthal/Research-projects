x = float(input("valor x: "))
y = float(input("valor y: "))

if (x>0 and y>0):
	print("Q1")
elif (y>0 and x<0):
	print("Q2")
elif (y<0 and x<0):
	print("Q3")
elif (y<0 and x>0):
	print("Q4")
	
if((x==y) and (y==0)):
	print("Origem")
elif ((y!=x) and (x==0)):
	print("Eixo Y")
elif ((x!=y) and (y==0)):
	print("Eixo X")
	