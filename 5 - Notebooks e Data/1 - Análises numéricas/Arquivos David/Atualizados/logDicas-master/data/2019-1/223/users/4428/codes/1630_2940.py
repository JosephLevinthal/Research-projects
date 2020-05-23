Vi = float(input("Valor inicial: "))
j = float(input("Taxa de Juros: "))
n = float(input("Numero de Meses: "))

Vf = (Vi*((1+j)**n))

print(round(Vf, 2))