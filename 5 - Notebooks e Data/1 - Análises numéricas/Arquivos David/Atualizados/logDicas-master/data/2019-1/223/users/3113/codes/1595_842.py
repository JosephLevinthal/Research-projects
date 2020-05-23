# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
num =int(input("numero inteiro de quatro digitos:"))

n = num // 1 % 10
u = num // 10 % 10
p = num // 100 % 10
q = num // 1000 % 10

qpun=q+p+u+n

print(qpun)