# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = int(input('n1: '))
b = int(input('n2: '))
c = int(input('n3: '))
d = min(a,b,c)
e = max(a,b,c)
m = ( a + b + c) - e - d

print(d)
print(m)
print(e)