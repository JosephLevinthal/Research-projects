# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
x= int(input("escolha um numero "))
y= int(input("escolha um numero "))
z= int(input("escolha um numero "))
menor_numero=min(x, y, z)
maior_numero=max(x, y, z)
intermediario= x+y+z-menor_numero-maior_numero
print(menor_numero)
print(intermediario)
print(maior_numero)