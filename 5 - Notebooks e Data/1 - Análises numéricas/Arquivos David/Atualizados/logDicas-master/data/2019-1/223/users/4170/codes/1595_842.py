# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
num = int(input("Insira um numero: ")) 
a = num // 1000
b = (num // 100) % 10
c = (num // 10) % 10
d = num % 10
print(a + b + c + d)