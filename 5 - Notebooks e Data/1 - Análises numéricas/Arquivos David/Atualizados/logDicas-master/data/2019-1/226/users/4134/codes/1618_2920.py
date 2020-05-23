peso = float(input("Quantas gramas possui seu prato? "))
beb = int(input("Numero de bebidas: "))
sobm = int(input("Numero de sobremesas: "))

precoa = 26.90
precob = 3.50
precoc = 3.00

x = peso/1000

eq = (precoa*x) + (beb*precob) + (precoc*sobm)
print(round(eq, 2))