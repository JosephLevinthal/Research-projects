valor = float(input("Ticket disponiveis: "))
Q1 = int(input("Quantidades desejadas: "))
V1 = float(input("Valor dos tickets: "))
Q2 = int(input("Passes: "))
V2 = float(input("Valor dos passes: "))

if (valor >= Q1 * V1 + Q2 * V2):
	msg = "suficiente"
else:
	msg = "insuficiente"
# Saida
print(msg.upper())
