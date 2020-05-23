# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
d=int(input("Digite um numero: "))
a=d // 1000
b=(d // 100) % 10
c=(d // 10) % 10
d= d % 10
soma=a + b + c + d
print(soma)
