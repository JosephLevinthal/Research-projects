n = float(input("valor do n de mols: "))
v = float(input("valor do volume: "))
t = float(input("valor da temp.: "))
t1 = t + 273.1
r = 0.082057

p = ((n*r*t1)/v)

print(p)