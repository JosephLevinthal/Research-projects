a = float(input("Quantidade de horas extras:"))
b = float(input("Quantidade de faltas:"))

print(a," extras e ",b," de falta")

c = a - (1/4 * b)

if(c<=400):
	g =100.0
	print("R$",round(g,2))
elif(c>400):
	g=500.0
	print("R$",round(g,2))