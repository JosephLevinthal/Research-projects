# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a=int(input("Escreva um numero:"))
b=a // 1000
c= a % 1000
d=c//100
e=c%100
f=e//10
g=e%10
h=(b+d+f+g)
print(h)