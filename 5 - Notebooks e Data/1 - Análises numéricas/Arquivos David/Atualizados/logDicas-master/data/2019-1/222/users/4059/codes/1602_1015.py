# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a=int(input())
b=int(input())
c=int(input())

total = a+b+c

aux =  min(a,b,c)+max(a,b,c)
Inter = total - aux

print(min(a,b,c))
print(Inter)
print(max(a,b,c))