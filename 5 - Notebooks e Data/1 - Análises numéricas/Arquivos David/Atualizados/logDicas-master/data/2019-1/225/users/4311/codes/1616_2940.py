vi = float(input("Valor inicial emprestado: "))
j = float(input("Taxa de juros: "))
n = float(input("Meses em que o dinheiro ficou emprestado: "))

vf = vi*(1+j)**n

print(round(vf,2))