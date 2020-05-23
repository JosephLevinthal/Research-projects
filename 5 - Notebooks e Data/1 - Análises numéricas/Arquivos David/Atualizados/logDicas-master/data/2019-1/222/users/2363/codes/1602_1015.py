# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
x=int(input("x e  "))
y=int(input("y e  "))
z=int(input("z e  "))
mini=min(x,y,z)
maxi=max(x,y,z)
meio=(x+y+z)-mini - maxi
print(mini)
print(meio)
print(maxi)