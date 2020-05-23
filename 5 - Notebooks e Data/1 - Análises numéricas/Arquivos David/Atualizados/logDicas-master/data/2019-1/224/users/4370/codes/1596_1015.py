# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
n_inteiros1 = int(input("primeiro numero"))
n_inteiros2 = int(input("segundo numero"))
n_inteiros3 = int(input("terceiro numero"))
n_max = max(n_inteiros1,n_inteiros2,n_inteiros3)
n_min = min(n_inteiros1,n_inteiros2,n_inteiros3)
n_medio = (n_inteiros1 + n_inteiros2 + n_inteiros3) - (n_max + n_min)
print(n_min)
print(n_medio)
print(n_max)
