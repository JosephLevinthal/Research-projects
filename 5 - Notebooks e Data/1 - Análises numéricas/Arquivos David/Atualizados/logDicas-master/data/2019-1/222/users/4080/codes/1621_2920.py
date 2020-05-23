from math import*
g = float(input("quantas gramas tem seu prato?: "))
b = float(input("quantas bebidas?: "))
s = float(input("quantas sobremesas?: "))
k = float(g/1000)
l = k*26.90
l1 = b*3.5
l2 = s*3.0
l3 = (l+l1+l2)
print(round(l3,2))
