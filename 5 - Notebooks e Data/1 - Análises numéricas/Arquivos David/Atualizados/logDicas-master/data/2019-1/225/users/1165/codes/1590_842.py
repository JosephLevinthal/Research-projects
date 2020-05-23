var = int(input("Numero: "))

soma = 0

while (var != 0):
    resto = var % 10
    var = (var - resto)//10
    soma = soma + resto
print(soma)
