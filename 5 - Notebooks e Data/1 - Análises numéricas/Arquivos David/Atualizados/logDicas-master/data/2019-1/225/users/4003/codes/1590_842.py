# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.valor =
v = int(input("digite o numero"))
a= v//1000#Milhar
b= v//100%10#centena
c= v//10%10#dezena
d= v//1%10#unidade
print(a+b+c+d)