# Entradas
num = int(input("Determine: "))
# Variavel
a = num // 1000
b = num // 100 - a*10
c = num // 10 - (num // 100) * 10
d = num - (num // 10) * 10
# Digito Verificador
con1 = a * 5
con2 = b * 4
con3 = c * 3
con4 = d * 2
# Variavel de Soma
soma = con1 + con2 + con3 + con4
resto = soma % 11
# Saida
print(resto)