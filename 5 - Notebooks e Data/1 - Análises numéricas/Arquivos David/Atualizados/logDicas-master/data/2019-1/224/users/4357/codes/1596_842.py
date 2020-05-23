# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
numero=int(input("digite um numero de 4 algarismo"))
n1= numero // 1000
n2= (numero%1000)//100
n3= ((numero % 1000 )% 100) // 10
n4= ((( numero % 1000 ) % 100 ) % 10)
soma=(n1 + n2 + n3 + n4)
print(soma)