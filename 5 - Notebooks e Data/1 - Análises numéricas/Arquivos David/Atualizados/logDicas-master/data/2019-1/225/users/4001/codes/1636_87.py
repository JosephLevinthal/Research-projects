# Entradas
n1 = int(input("N1: "))
n2 = int(input("N2: "))
n3 = int(input("N3: "))
# Condicoes
if (n1 < n2 and n1 < n3):
	menor = n1
if (n2 < n1 and n2 < n3):
	menor = n2
if (n3 < n1 and n3 < n2):
	menor = n3
# Saida
print(menor)
					


