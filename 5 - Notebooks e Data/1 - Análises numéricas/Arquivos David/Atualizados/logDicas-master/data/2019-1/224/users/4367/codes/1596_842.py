# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
numero= int(input("escolha um numero inteiro com 4 algarismos "))
x= int(numero//1000)
y= int(numero%1000//100)
z= int(numero%1000%100//10)
t= int(numero%10)
soma= x+y+z+t
print(soma)