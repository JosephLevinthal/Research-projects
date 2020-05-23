# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a=int(input("Escrevava uma sequencia numerica de 4 digitos:"))
b=int(a/10)
c=int(a/100)
d=int(a/1000)
f=c%10
e=a%10
g=b%10

print(d+f+g+e)