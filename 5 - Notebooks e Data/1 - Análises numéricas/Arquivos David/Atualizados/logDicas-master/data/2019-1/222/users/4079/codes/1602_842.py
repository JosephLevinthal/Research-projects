# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu comu
numero = int(input("Digite um numero de 4 digitos:"))
a= numero // 1000
b= numero % 1000
c= b // 100
d = b % 100
e = d // 10
f = d % 10
print(a + c + e + f)


