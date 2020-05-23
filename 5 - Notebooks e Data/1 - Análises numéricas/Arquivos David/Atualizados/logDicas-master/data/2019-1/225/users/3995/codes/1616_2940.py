Vi=float(input("valor inicial:"))
j=float(input("taxa de juros:"))
n=float(input("tempo em meses:"))
Vf=Vi*(1+j)**n
print(round(Vf, 2))