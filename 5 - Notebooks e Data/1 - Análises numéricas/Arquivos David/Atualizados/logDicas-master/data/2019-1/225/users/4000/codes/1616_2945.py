from math import*
d = float(input("valor do diametro?"))
t = float(input("tamanho da espessura?"))
p = int(input("quantidade?"))
m = (d**2 *t * pi* p)/ 4
print(round(m, 2))