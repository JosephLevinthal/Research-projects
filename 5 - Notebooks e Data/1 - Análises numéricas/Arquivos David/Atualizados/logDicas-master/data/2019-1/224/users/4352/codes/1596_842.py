# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

valor = int(input("Digite um numero de 4 digitos: "))
x = int(valor//1000%100%10)
y = int(valor//100%10)
z = int(valor//10%10)
k = int(valor%10)
soma = x+y+z+k
print(soma) 
