# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
x = int(input("Digite um numero: "))
y = x//1%10
y1 = x//10%10
y2 = x//100%10
y3 = x//1000%10
print(y+y1+y2+y3)
