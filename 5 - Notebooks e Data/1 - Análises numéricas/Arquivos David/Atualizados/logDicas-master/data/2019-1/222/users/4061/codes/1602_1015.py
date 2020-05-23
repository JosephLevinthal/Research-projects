# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = int(input("digite o primeiro numero"))
b = int(input("digite o segundo numero"))
c = int(input("digite o terceiro numero"))
menor = min(a,b,c)
maior = max(a,b,c)
medio = (((a+b+c)-menor)-maior)
print(menor)
print(medio)
print(maior)


