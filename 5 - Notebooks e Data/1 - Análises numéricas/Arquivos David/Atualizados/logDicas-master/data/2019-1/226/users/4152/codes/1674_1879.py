# Ao testar sua solução, não se limite ao caso de exemplo.
E = float(input("Digite aqui o total de horas extras: "))
F = float(input("Digite aqui o total de horas nao trabalhadas: "))
H = E - ((1/4) * F)
if (H <= 400):
	G = 100.0
else:
	G = 500.0
print (E, "extras", "e", F, "de falta")
print ("R$", G)
	
	