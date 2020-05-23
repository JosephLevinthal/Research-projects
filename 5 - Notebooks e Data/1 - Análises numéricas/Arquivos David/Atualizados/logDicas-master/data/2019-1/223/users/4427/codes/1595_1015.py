# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

# Leia tres numeros inteiros
x = int (input("insira um numero: "))
y = int (input("insira outro numero: "))
z = int (input("insira mais um numero:"))

a = min(x,y,z)
c = max(x,y,z)

b = (((x+y+z)-a)-c)

# impressao dos valores crescentes
print(a)
print(b)
print(c)
