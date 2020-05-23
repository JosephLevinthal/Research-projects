# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
x=int(input("entre com um numero de 4 digitos:"))

a=x%1000
u=x//1000

b=a%100
v=a//100

c=b%10
p=b//10

d=c%1
q=c//1

r=u+v+p+q

print(r)

