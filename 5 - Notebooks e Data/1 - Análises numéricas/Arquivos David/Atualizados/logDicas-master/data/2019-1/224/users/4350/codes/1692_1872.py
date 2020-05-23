x = float(input("valor de x"))
y = float(input("valor de y"))

if x>0 and y>0:
	r = "Q1"
elif x<0 and y>0:
	r = "Q2"
elif x<0 and y<0:
	r = "Q3"
elif x>0 and y<0:
	r = "Q4"
elif x==0 and y>0 or y<0:
	r = "Eixo Y"
elif y==0 and x>0 or x<0:
	r = "Eixo X"
elif y==0 and x==0:
	r = "Origem"
print(r)