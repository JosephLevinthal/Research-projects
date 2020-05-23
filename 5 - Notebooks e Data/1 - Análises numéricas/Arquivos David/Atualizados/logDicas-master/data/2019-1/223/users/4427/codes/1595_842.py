# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

# Digitar quatros numeros
var = int(input("Digite quatro numeros: "))

a = var//1000%10
b = var//100%10
c = var//10%10
d = var//1%10

soma_digitos = a + b + c + d

print(soma_digitos)