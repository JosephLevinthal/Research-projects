# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

n=int(input("numero inteiro de quatro digitos: "))
a=(n%10)
b=(n//10)%10
c=(n//10)//10%10
d=(n//1000)
print(a+b+c+d)

