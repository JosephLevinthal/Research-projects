# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = int(input("digite um numero: "))
b = int(input("digite um numero: "))
c = int(input("digite um numero: "))
menor = min(a,b,c)
maior = max(a,b,c)
medio = a+b+c-maior-menor
print(menor,medio,maior)