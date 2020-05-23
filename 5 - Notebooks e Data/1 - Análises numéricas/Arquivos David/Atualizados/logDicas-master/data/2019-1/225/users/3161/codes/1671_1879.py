E= float(input("horas extras:"))
F= float(input("horas faltando:"))
H= E-((1/4)*F)
if(H>400):
	G=round(500.00, 2)
else:
	G= round(100.00, 2)
print(E,"extras e", F, "de falta")
print("R$", G)