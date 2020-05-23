# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a= int(input("insira o valor de A:"))
b= int(input("insira o valor de B:"))
c= int(input("insira o valor de C:"))
m=min(a,b,c)
M= max(a,b,c)
s=(a+b+c)-m-M
print(m)
print(s)
print(M)