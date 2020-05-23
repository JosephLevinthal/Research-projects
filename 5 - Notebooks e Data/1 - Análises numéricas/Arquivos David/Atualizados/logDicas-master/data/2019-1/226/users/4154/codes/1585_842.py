# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = int(input("entre com um valor de quatro digitos: "))
b = (a//1000) 

c = (a - b*1000)//100

d = ((a - b*1000) - c*100)//10

e = ((a - b*1000) - c*100)%10

print(b+c+d+e)