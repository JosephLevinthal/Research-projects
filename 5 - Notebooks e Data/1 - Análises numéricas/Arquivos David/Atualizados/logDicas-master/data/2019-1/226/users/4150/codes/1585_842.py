# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

num = int(input("digite um numero de quatro digitos: "))

a = (num//1000)

b = (num//100)
b1 = (b%10)

c = (num%1000)
c1 = (c%100)
c2 = (c1//10)

d = (num%10)



print(a+b1+c2+d)
