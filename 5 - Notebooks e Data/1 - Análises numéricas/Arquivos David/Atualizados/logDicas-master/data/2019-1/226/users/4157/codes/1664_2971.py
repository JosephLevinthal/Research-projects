j = float(input("taxa de juros:"))
vp = float(input("valor do apartamento:"))
t = 36
qi = 1500.0
qf = qi*(1 + j)**t

if(qf >= vp):
	print(round(qf, 2))
	print("Sim")
else:
	print(round(qf, 2))
	print("Nao")
	