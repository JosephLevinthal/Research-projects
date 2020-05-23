# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = int(input())
b = int(input())
c = int(input())

menor = min(a,b,c)
maior = max(a,b,c)
meio = (a+b+c) - (maior+menor)

print(menor,meio,maior)