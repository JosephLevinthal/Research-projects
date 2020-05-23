import math
n = int(input("Informe a quantidade de termos: "))

resultado = 0
cont = 0

while cont < n:
    resultado += + 1/math.factorial(cont)
    cont = cont + 1

print(round(resultado,8))