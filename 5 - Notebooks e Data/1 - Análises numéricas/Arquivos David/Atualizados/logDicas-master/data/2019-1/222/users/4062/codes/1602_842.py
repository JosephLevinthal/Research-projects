# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
num = int(input("qualquer inteiro de quatro digitos: "))
a = num//1%10
b = num//10%10
c = num//100%10
d = num//1000%10
print(a+b+c+d)