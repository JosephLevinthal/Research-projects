xa=float(input("Insira o valor de Xa:"))
xb=float(input("Insira o valor de Xb:"))
ya=float(input("Insira o valor de Ya:"))
yb=float(input("Insira o valor de Yb:"))

ab=(xb-xa)**2 + (yb-ya)**2
t=ab**0.5

print(round(t, 3))