# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
A = int(input("Primeiro valor:"))
B = int(input("Segundo valor:"))
C = int(input("Terceiro valor:"))

I = A + B + C - min(A,B,C) - max(A,B,C)
print((min(A,B,C)),(I),(max(A,B,C)))



