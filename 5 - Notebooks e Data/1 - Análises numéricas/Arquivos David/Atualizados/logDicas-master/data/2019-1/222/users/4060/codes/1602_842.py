# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a=int(input("numero com quatro digitos: "))
#1º
x=(a//1000)
#2º
y=(a%1000)
z=(y//100)
#3°
q=(a%100)
g=(q//10)
#4º
h=(a%10)
i=(h//1)
print(x+z+g+i)
