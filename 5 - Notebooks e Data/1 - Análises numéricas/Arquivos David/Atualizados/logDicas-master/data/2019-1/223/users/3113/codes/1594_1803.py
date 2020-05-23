# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
num =int(input("numero inteiro de quatro digitos:"))

n = num // 1 % 10
u = num // 10 % 10
p = num // 100 % 10
q = num // 1000 % 10

d1=n*2
d2=u*3
d3=p*4
d4=q*5

d1d2d3d4=(d1+d2+d3+d4)

p1=d1d2d3d4%11


print(p1)