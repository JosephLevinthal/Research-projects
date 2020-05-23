# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
x = int(input())
y = int(input())
z = int(input())

maxi = max (x, y, z)
mini = min (x, y, z)
inte = ((x + y + z) - maxi) - mini
print (min (x, y, z))
print(inte) 
print(max (x, y, z))

