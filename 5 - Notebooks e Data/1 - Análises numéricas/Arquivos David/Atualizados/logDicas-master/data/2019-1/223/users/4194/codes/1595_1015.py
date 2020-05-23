# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
n1=int(input("Digite um numero: "))
n2=int(input("Digite um segundo numero: "))
n3=int(input("Digite um terceiro numero: "))
print (min(n1,n2,n3))
print ((n1 + n2 + n3) - (min(n1,n2,n3) + max(n1,n2,n3)))
print (max(n1,n2,n3))