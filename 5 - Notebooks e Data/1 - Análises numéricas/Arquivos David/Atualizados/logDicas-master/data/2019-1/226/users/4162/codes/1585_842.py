# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
num=int(input("escolha um numero de 4 digitos: "))
a= num//1 % 10
b=num//10%10
c= num//100%10
d=num//1000%10
print (a+b+c+d)