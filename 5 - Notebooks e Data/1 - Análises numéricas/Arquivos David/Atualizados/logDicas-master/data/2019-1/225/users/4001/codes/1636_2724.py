# Entradas
n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
n3 = int(input("Numero 3: "))
# Condicoes
if (n1 > n2 and n1 < n3):
	meio = n1
if (n1 < n2 and n1 > n3):
	meio = n1
if (n2 > n1 and n2 < n3):
	meio = n2
if(n2 < n1 and n2 > n3):
	meio = n2
if (n3 > n1 and n3 < n2):
	meio = n3
if(n3 < n1 and n3 > n2):
	meio = n3
print(meio)