# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

# n = input("Digite um numero inteiro: ")

# print(sum(int(i) for i in n))

n = int(input("Digite um numero inteiro: "))

soma = 0

while (n > 0):

    resto = n % 10
    n = n // 10
    soma = soma + resto

print(soma)