# Ao testar sua solução, não se limite ao caso de exemplo.
E = float(input("Digite o numero de horas extras: "))
F = float(input("Digite o numero de faltas: "))
print(E, "extras", "e", F, "de falta")
H= E-(1/4)*F
if(H>400):
	mensagem=round(500.00,2)
else:
	mensagem=round(100.00,2)
print("R$", mensagem)
	