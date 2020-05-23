Vi = float(input("digite o valor inicial"))
j = float(input("digite a taxa de juros"))
n = float(input("digite o numero de meses"))
Vf = Vi*(1+j)**n
print(round(Vf, 2))