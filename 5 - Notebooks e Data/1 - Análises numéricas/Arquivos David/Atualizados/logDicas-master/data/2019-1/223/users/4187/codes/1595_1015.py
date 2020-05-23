# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
x= int(input("insira um valor x:"))
y= int(input("insira um valor y:"))
z= int(input("insira um valor z:"))

l= min(x,y,z)
m= max(x,y,z)

print(min(x,y,z))
print((x+y+z)-l-m)
print(max(x,y,z))