# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = float(input("comprimento a do lado de um triangulo:"))
b = float(input("comprimento b do lado de um triangulo:"))
c = float(input("comprimento c do lado de um triangulo:"))
s = (a+b+c)/2
area = ((s*(s-a))*(s-b)*(s-c))**1/2
a1 = s-a
a2 = s-b
a3 = s-c
a4 = a1*a2*a3
a5 = a4*((a+b+c)/2)
a6 = a5**0.5
print(round(a6, 5)) 