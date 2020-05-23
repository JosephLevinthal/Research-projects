# Entradas
num = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
num3 = int(input("Numero 3: "))
# Condicoes
if (num > num2 and num > num3):
	maior = num
if (num2 > num and num2 > num3):
	maior = num2
if (num3 > num and num3 > num2):
	maior = num3
# Saida
print(maior)
