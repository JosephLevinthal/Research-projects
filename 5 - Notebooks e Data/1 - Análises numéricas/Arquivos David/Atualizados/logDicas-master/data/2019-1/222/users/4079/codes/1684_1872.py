# Ao testar sua solução, não se limite ao caso de exemplo.
from math import*
x=int(input("x: "))
y=float(input("y: "))
if(x==0 and y==0):
	print("Origim")
elif(y==0):
	print("Eixo x")
elif(x==0):
	print("Eixo y")
elif(x>0 and y>0):
	print("Q1")
elif(x<0 and y>0):
	print("Q2")
elif(x<0 and y<0):
	print("Q3")
elif(x>0 and y<0):
	print("Q4")