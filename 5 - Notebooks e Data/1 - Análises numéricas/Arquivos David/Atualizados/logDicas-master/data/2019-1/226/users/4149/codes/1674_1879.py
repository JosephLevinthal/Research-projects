h= float(input("extras "))
f= float(input("faltas "))
print(h,"extras e",f,"de falta")

i=h-((1/4)*f)


if(i>400):
	print("R$",500.00)
elif(i<=400):
	print("R$",100.00)