# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a=int(input("escreva um numero"))
b=int(input("escreva um numero"))
c=int(input("escreva um numero"))
menor=min(a,b,c)
maior=max(a,b,c)
soma=(a+b+c)
soma= soma- menor
soma= soma - maior
print(int(menor))
print(int(soma))
print(int(maior))