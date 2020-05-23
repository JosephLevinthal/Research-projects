# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
numero = int(input("Digite um numero de quatro digitos: "))
a = numero // 1000
a1 = numero % 1000
b = a1 // 100
b1 = a1 % 100
c = b1 //10
c1 = b1 % 10
d = c1 
print(a + b + c + d)