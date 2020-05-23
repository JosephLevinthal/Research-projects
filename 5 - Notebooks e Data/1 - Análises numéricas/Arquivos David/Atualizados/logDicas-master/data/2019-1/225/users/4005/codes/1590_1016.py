# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a= float(input("a:"))
b= float(input("b:"))
c= float(input("c:"))
s= (a+b+c)
j= s/2
A=(j*(j-a)*(j-b)*(j-c))**0.5
print(round((A),5))