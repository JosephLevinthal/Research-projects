# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
numero = int(input("digite o numero"))
a = numero//1000
b = (numero//100)%10
c = ((numero//10)%100)%10
d = (((numero//1)%1000)%100)%10
soma = a+b+c+d
print(soma)