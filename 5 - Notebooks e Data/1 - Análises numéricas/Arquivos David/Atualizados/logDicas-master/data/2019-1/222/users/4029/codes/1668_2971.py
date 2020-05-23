x= float(input("Qual a taxa de juros? "))
y= float(input("Qual o valor do apartamento? "))
qf = 1500.00 * ((1 + x) ** 36)
if (qf >= y):
	print(round(qf, 2))
	print("Sim")
else: 
	print(round(qf, 2))
	print("Nao")