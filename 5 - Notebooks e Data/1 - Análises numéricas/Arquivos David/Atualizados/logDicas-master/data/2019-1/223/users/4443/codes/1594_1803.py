# Leitura dos numeros digitados a partir do teclado:
var = int(input("Digite um numero com quatro algarismos: "))

m = var // 1000
r1 = var % 1000
c = r1 // 100
r2 = r1 % 100
d = r2 // 10
r3 = r2 % 10
u = r3

# calculo do digito verificador
soma = u*2 + d*3 + c*4 + m*5
dv = soma % 11
print(dv)
