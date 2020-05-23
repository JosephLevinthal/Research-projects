# Entradas
qicv = int(input("Determine o valor: "))
qils = int(input("Determine o valor: "))
pmv = int(input("Determine o valor: "))
pml = int(input("Determine o valor: "))
# Percentual
percV = pmv / 100
percL = pml / 100
# Variavel contadora
dia = 0
# laço
while (qils <= 2*qicv):
	qils = qils + (qils * percL)
	qicv = qicv + (qicv * percV)
	dia = dia + 1
#saida
print(dia)