# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
n = int(input("numero inteiro: "))

a = n // 1000

b= (n // 100) % 10 

c =(n // 10) % 10

d = n % 10

soma = a + b + c + d

print(soma)