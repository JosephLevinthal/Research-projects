# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
n=int(input("numero de quatro digitos: "))
n1=n//1000
n2=n%1000
n3=n2//100
n4=n2%100
n5=n4//10
n6=n4%10
print(n1+n3+n5+n6)