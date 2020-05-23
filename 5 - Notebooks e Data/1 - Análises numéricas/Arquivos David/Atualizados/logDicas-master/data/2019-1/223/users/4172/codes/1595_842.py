# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
x=int(input("numero de 4 digitos: "))

s1=x//1000
s2=(x//100)%10
s3=(x//10)%10
s4=x%10
print(s1+s2+s3+s4)
 