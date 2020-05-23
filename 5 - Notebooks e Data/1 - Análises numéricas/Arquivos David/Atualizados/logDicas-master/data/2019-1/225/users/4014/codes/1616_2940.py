vi=float(input("valor inicial: "))
j=float(input("taxa de juros: "))
n=float(input("tempo em meses: "))
vf=vi*(1+j)**n
print(round(vf, 2))