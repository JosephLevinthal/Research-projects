# Leitura dos numeros digitados a partir do teclado:
var = int(input("Digite um numero com quatro algarismos: "))
soma = 0
while (var > 0):
    resto = var % 10
    var = var // 10
    soma = soma + resto

print(soma)

