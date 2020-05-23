# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

num1 = int(input("Valor1: "))
num2 = int(input("Valor2: "))
num3 = int(input("Valor3: "))

lista = (num1, num2, num3)
num4 = min(lista)
num5 = max(lista)
print(min(lista))

equacao = (num1 + num2 + num3 - num5 - num4)
print(equacao)

print(max(lista))