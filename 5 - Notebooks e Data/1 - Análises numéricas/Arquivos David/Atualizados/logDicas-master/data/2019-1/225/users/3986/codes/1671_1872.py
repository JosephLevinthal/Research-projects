# Ao testar sua solução, não se limite ao caso de exemplo.
x=float(input("ponto x :"))
y=float(input("ponto y: "))

if (x > 0) and (y > 0) :
	print("Q1")
elif ( x < 0) and (y > 0):
	print("Q2")
elif (x <0 ) and (y < 0) :
	print("Q3")
elif (x > 0) and (y < 0) :
	print("Q4")
elif (x == 0) and (y != 0) :
	print("Eixo Y")
elif (y == 0) and (x != 0) :
	print("Eixo X")

else :
	print("Origem")