# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a=int(input())
b=int(input())
c=int(input())
soma=a+b+c
maior=max(a,b,c)
menor=min(a,b,c)
soma= soma-maior
soma= soma-menor
print(min(a,b,c))
print(soma)
print(max(a,b,c))