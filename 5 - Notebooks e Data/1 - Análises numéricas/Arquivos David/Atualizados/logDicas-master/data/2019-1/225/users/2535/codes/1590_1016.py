# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = float(input())
b = float(input())
c = float(input())

S = (a + b + c)/2

A = (S*(S - a)*(S - b)*(S - c))**0.5

print(round(A, 5))