# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

# Leitura dos numeros digitados a partir do teclado:
var = int(input("Digite um numero com quatro algarismos: "))

#soma = 0

#while (var > 0):

  #  resto = var % 10
   # var = var // 10
    #soma = soma + resto

#print(soma)

# segunda forma de resolucao
m = var // 1000
r1 = var % 1000
c = r1 // 100
r2 = r1 % 100
d = r2 // 10
r3 = r2 % 10
u = r3

print(m + c + d + u)

		