#3141|10 = 
# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
num = int(input())

n1 = int(num%10)
n2 = int((num%100)/10)
n3 = int((num%1000)/100)
n4 = int(num/1000)

plus = n1 + n2 + n3 + n4

print(plus)
print(n1)
print(n2)
print(n3)
print(n4)