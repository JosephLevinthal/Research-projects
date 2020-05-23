Vi = float(input("digite um valor: "))
j = float(input ("digite uma taxa: "))
n = float(input("digite a quantidade de meses: "))

Vf = Vi * (1 + j) ** n

print(round(Vf, 2))