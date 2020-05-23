# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = int(input("numero inteiro 1:"))
b = int(input("numero inteiro 2:"))
c = int(input("numero inteiro 3:"))
x = min(a,b,c)
z = max(a,b,c)
y = a + b + c - x - z
print(x)
print(y)
print(z)