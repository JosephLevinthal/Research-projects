# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
valor=int(input("Digite um numero de 4 digitos"))
a=valor//1000
b=(valor-(a*1000))//100
c=(valor-(a*1000)-(b*100))//10
d=(valor-(a*1000)-(b*100)-(c*10))

total=a+b+c+d

print(total)