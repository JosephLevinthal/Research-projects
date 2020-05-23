# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
num = float(input("Quatro digitos: ")) 

X = num // 1000
x = num % 1000
Y = x // 100
y = x % 100
Z = y // 10
z = y % 10

soma = X + Y + Z + z
print(soma)



