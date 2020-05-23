A = int(input("Qtd de votos AR: "))
D = int(input("Qtd de votos DO: "))
a = (A * 100)/ (D + A)
d = (D * 100)/ (D + A)
# Condicoes
if (A > D):
	msg = "Ambrosio Rutra"
	msg2 = a
else:
	msg = "Demelza Olecram"
	msg2 = d
# Saidas
print(msg)
print(round(msg2, 2))
