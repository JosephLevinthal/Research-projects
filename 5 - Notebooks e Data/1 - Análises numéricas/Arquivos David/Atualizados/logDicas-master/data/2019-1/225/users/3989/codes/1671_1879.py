ne = float(input("Digite numero de horas extras:"))
nf = float(input("Digite o numero de faltas:"))

print( ne, "extras", "e", nf, "de falta")

H = ne - 1/4 * nf
if (H>400):
	G = 500.00
	print("R$ ", round(G, 2))
elif (H<=400):
	G = 100.00
	print("R$ ", round(G, 2)) 
