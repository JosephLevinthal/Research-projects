# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
n = int(input("digita caralho: "))

x1 = n//1000
x2 = n//100	- (n//1000)*10
x3 = n//10 - (n//100)*10
x4 = n//1 - (n//10)*10
baiano = x1 + x2 +x3 +x4
print(baiano)