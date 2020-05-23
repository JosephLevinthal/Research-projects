# Ao testar sua solução, não se limite ao caso de exemplo.
x = float(input("digite x:" ))
y = float(input("digite y:" ))
if(x > 0 and y > 0):
	print("Q1")
if(x > 0 and y < 0):
	print("Q4")
if(x < 0 and y < 0):
	print("Q3")
if(x < 0 and y > 0):
	print("Q2")
if(x == 0 and y == 0):
	print("Origem")