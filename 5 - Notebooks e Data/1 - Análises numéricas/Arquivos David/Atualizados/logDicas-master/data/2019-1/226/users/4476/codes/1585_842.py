# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = int(input("digite: "))
x = a//1000
y = a//100 - (a//1000)*10
z = a//10 - (a//100)*10
d = a -(a//10)*10
print(x+y+z+d)