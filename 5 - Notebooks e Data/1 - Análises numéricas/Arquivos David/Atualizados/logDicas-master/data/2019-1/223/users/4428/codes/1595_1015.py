# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

var1 = int(input("Digite um numero: "))
var2 = int(input("Digite um numero: "))
var3 = int(input("Digite um numero: "))
menor = min(var1, var2, var3)
maior = max(var1, var2, var3)
valor_inter = (((var1+var2+var3)-menor)-maior)

print(min(var1, var2, var3))
print(valor_inter)
print(max(var1, var2, var3))

