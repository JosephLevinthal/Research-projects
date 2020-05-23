# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a= int(input("digite um numero com quatro digitos: "))
b= a//1000
b1= a%1000
c= b1//100
c1= b1%100
d= c1//10
d1= c1%10
e= d1//1

x= (b+c+d+e)
print(x)