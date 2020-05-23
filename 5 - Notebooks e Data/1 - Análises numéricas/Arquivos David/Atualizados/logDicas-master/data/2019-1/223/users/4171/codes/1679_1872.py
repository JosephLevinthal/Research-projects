x = float(input("x: "))
y = float(input("y: "))

if x == 0 and x == y:
	a ="Origem"

elif x > 0 and y > 0:
	a ="Q1"
elif x < 0 and y > 0:
	a ="Q2"
elif x < 0 and y < 0:
	a ="Q3"
elif x > 0 and y < 0:
	a ="Q4"
	
elif y == 0 and x != 0:
	a ="Eixo X"
elif x == 0 and y != 0:
	a ="Eixo Y"
	
print(a)