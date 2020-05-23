# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = float(input("Insira o lado a:"))
b = float(input("Insira o lado b:"))
c = float(input("Insira o lado c:"))
s = (a + b + c)/2
import math
area = float(math.sqrt(s*(s-a)*(s-b)*(s-c)))
print(round(area,5))