# Ao testar sua solução, não se limite ao caso de exemplo.
ne = float(input("Digite nmr de hrs extras: "))
nf = float(input("Digite nmr de hrs q faltou: "))

print(ne, "extras", "e", nf, "de falta")

H = (ne) - 1/4 * (nf)

if(H>400):
	G = 500.00
	print("R$", round(G,2))
elif(H<=400):
	G = 100.00
	print("R$", round(G,2))
