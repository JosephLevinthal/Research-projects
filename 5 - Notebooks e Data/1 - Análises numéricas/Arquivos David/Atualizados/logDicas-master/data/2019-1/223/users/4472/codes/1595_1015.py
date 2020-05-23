# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

var1 = input("Informe o primeiro numero: ")
var2 = input("Informe o segundo numero: ")
var3 = input("Informe o terceiro numero: ")

num1 = int(var1)
num2 = int(var2)
num3 = int(var3)

menor = min(var1, var2, var3)
me = int(menor)
maior = max(var1, var2, var3)
ma = int(maior)
meio = (num1 + num2 + num3) - (me + ma)

print (menor, meio, maior)