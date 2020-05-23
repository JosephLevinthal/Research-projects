# Ao testar sua solução, não se limite ao caso de exemplo.
E = float(input("Digite o numero de horas extras: "))
F = float(input("Numero de horas que o funcionario faltou: "))
print(E, "extras e", F, "de falta")

G = (E) - 1/4*(F)
if(G > 400):
	print("R$", 500)
else:
	print("R$", 100)
