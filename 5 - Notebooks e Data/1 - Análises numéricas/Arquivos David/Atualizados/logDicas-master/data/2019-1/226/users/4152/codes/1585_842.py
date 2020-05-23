# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
num = int(input("Digite aqui seu numero: "))

var1 = int(num // 1000)

var2 = int(num // 100) % 10

var3 = int(num // 10) % 10

var4 = int(num % 10)

total = int(var1 + var2 + var3 + var4)

print(total)