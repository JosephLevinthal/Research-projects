# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
num1 = int(input("Digite os quatro dfigitos:"))

x = int(num1/1000)
y = int(num1 % 10)
k = int(num1 /100)
z= int(k%10)
l= int(num1/10)
j = int(l%10)
print(x + y + z + j)