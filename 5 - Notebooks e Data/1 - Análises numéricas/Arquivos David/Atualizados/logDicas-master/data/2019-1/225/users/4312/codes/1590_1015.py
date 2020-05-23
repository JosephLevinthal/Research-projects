# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = int(input("qual o valor de a? "))
b = int(input("qual o valor de b? "))
c = int(input("qual o valor de c? "))

#valor intermediario
var = a + b + c
x = (var -(min(a,b,c)) - max(a,b,c))

print(int(min(a,b,c)))
print(int(x))
print(int(max(a,b,c)))

