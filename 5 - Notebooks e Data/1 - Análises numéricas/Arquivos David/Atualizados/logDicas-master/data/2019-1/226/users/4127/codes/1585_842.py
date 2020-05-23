# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
n=int(input("escreva um numero inteiro de quatro digitos: "))
x1=(n//1000)
x2=((n//100)-x1*10)
x3=((n//10)-(n//100)*10)
x4=(n-(n//10)*10)
print(x1+x2+x3+x4)