# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = int(input("primeiro numero: "))
b = int(input("segundo numero: "))
c = int(input("terceiro numero: "))
minimo = min(a, b, c)
maximo = max(a, b, c)
intermediario = (a + b + c - b - a)
print(minimo, intermediario, maximo)

