# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
num =int(input("numero inteiro de quatro"))

a = num // 1 % 10
b = num // 10 % 10
c = num // 100 % 10
d = num // 1000 % 10 

abcd=a+b+c+d

print (abcd)