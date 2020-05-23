vi = float(input("Entre com o valor inicial: "))
j = float(input("Entre com a taxa de juros: "))
n = float(input("Entre com o numero de meses: "))

vf = vi * ((1 + j) ** n)

print(round(vf, 2))