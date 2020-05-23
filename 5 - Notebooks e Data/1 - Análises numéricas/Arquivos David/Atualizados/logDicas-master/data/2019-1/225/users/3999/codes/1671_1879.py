# Ao testar sua solução, não se limite ao caso de exemplo.
E=float(input("Hr extras: "))
F=float(input("Hr faltas: "))
H=E-(F/4)
if(H>400):
	G=500.0
else:
	G=100.0
print(E,"extras e ",F,"de falta")
print("R$",round(G,2))