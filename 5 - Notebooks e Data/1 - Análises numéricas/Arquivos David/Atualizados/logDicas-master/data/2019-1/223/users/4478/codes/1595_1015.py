# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
menor = min(a,b,c)
maior = max(a,b,c)
inter = a+b+c-menor-maior
print(menor)
print(inter)
print(maior)