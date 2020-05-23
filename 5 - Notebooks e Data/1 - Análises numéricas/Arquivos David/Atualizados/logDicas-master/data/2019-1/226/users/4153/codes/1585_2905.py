# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a=float(input("Insira o comprimento dos lados: "))
b=float(input("Insira o comprimento dos lados: "))
c=float(input("Insira o comprimento dos lados: "))

s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5

print(round(area,5))