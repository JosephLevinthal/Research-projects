# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

#Ler os valores de entrada
from math import*
a = float(input("Entrar com o primeiro valor: "))
b = float(input("Entrar com o segundo valor: "))
c = float(input("Entrar com o terceiro valor: "))

# calcular semiperimetro
s = (a + b + c)/2

# calcular a area
A = sqrt(s*(s-a)*(s-b)*(s-c))

#impressao da area
print (round (A,5))