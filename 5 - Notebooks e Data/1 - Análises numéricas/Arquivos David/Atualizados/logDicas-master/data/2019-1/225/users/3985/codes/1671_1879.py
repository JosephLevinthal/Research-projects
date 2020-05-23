# Ao testar sua solução, não se limite ao caso de exemplo.
ne= float(input("NUMERO DE HORAS EXTRAS: "))
nt= float(input("NUMERO DE HORAS NAO TRABALHADAS: "))
h= (ne)-1/4*(nt)

print(ne,"extras","e",nt,"de falta")

if (h>400):
	print("R$", round(500.00, 2))
elif (h<=400):
	print("R$", round(100.00, 2))