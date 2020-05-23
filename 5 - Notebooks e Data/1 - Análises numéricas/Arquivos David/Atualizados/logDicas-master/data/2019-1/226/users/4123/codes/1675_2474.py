# Teste seu código com o dia do seu nascimento. Deu certo? E o dia de hoje?

# Que importante cientista nasceu em 4 de janeiro de 1643?
sem = ["sabado","domingo","segunda","terca","quarta","quinta","sexta"]
d = int(input())
m = int(input())
ano = int(input())
h = d + 13*(m+1)/5 + ano%100 + (ano%100)/4 + ano/100/4 + 5*ano/100
print(sem[int(h)])