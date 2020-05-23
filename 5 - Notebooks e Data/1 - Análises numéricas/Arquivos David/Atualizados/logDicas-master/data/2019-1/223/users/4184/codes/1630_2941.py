Vi=int(input("valor inicial: "))
j=float(input("taxa de juros: "))
n=int(input("numero do investimento: "))
Vf=Vi*(1+j)**n
print(round(Vf,2)