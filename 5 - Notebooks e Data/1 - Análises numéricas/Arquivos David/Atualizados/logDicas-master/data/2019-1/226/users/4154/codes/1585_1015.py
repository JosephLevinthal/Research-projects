# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as megens de erro. Elas ajudam a corrigir seu codigo.

a = int(input('digite o primeiro valor: '))
b = int(input('digite o segundo valor: '))
c = int(input('digite o terceiro valor: '))
d = a+b+c -(min(a,b,c)+max(a,b,c))

print(min(a,b,c))
print(d)
print(max(a,b,c))