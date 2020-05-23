# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

inteiro = int(input(" Digite um numero de 4 digitos: "))

a=inteiro//1000
b=(inteiro%1000)//100
c=((inteiro%1000)%100)//10
d=((inteiro%1000)%100)%10

print(a+b+c+d)