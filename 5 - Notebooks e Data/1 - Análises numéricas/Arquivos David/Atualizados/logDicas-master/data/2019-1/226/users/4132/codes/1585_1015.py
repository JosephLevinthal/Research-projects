# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

x1 = int(input("Digite o numero 1: "))
x2 = int(input("Digite o numero 2: "))
x3 = int(input("Digite o numero 3: "))

maior = max(x1,x2,x3)
menor = min(x1,x2,x3)
intermediario = (x1+x2+x3)-(menor+maior)

print(menor)
print(intermediario)
print(maior)