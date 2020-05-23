# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a=int(input("entre com um numero inteiro:"))
b=int(input("entre com um segundo numero inteiro:"))
c=int(input("entre com um terceiro numero inteiro:"))
x=min(a,b,c)
y=max(a,b,c)
w=a+b+c-min(a,b,c)-max(a,b,c)
print(x)
print(w)
print(y)