# Teste seu código com o dia do seu nascimento. Deu certo? E o dia de hoje?

# Que importante cientista nasceu em 4 de janeiro de 1643?
q = int(input("Dia do mes: "))
m = int(input("Mes: "))
ano = int(input("Ano: "))
h=(q + ((13*(m+1))/5)+(ano%100)+((ano%100)/4)+((ano/100)/4)+5*(ano%100))%7

print(int(h))