a = float(input("quantas gramas possui o prato? "))
b = int(input("quantidade de bebidas: "))
c = int(input("quantidade de sobremesas: "))
d = 26.90
e = 3.50
f = 3.00
g = a/1000
total = (g * d + b * e + c * f)
print(round(total, 2))