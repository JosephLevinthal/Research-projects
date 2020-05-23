# Ao testar sua solução, não se limite ao caso de exemplo.
x = float(input("coordenadas de x: "))
y = float(input("coordenadas de y: "))

if (x>0) and(y>0):
	c= "Q1"
elif(x<0)and(y>0):
	c= "Q2"
elif(x<0)and(y<0):
	c = "Q3"
elif(x>0)and(y<0):
	c= "Q4"
elif(y>0) or(y<0) and(x==0):
	c= "Eixo Y"
elif(x>0)or(x<0) and(y==0):
	c= "Eixo X"
elif(x==y==0):
	c= "Origem"
else: 
	c= "invalido"
print(c)