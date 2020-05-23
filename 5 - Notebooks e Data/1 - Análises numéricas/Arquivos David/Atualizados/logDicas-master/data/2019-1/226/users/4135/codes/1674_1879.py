# Ao testar sua solução, não se limite ao caso de exemplo.
E = float(input("Digite o numero de hrs extras trabalhadas:"))
F = float(input("Digite o numero de hrs faltas:"))
H = E - ((1/4)*F)
print(E,"extras e",F,"de falta")
if(E>0 and F>0):
	if(H>400):
		G= 500
	   print("R$",round(G,2))
	else:
		G = 100
	   print("R$",round(G,2))
else:
	G = 100
	print("R$",round(G,2))
	
	