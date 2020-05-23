j = float(input("taxa de juros: "))
va = float(input("valor do apartamento: "))
q0 = 1500
qf = round(q0*(1 + j)**36,2)

print(qf)

if(qf >= va):
	print("Sim")
else:
	print("Nao")