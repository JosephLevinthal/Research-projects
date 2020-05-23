he=float(input("he"))
hf=float(input("hf"))

h=(he)-(1/4*(hf))

if(h>400):
	g=500.00
	g=round(g,2)
	print(he,"extras e", hf ,"de falta")
	print("R$", g)
	

elif(h<=400):
	g=100.00
	g=round(g,2)
	print(he,"extras e", hf ,"de falta")
	print("R$",g)
	
	
