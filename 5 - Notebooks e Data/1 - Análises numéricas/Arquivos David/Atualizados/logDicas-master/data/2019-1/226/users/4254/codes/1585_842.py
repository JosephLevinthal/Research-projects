# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
num = int(input("Digite o numero inteiro: "))
soma = num // 1 % 10 + num // 10 % 10 + num // 100 % 10 + num // 1000 % 10
print(soma)