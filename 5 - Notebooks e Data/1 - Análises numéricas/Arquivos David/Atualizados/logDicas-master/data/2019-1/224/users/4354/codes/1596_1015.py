# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
numeros_inteiros1 = int(input("Digite o primeiro numero: "))
numeros_inteiros2 = int(input("Digite o segundo numero: "))
numeros_inteiros3 = int(input("Digite o terceiro numero: "))
numero_max = max(numeros_inteiros1,numeros_inteiros2,numeros_inteiros3)
numero_min = min(numeros_inteiros1,numeros_inteiros2,numeros_inteiros3)
numero_medio = (numeros_inteiros1 + numeros_inteiros2 + numeros_inteiros3) - (numero_max + numero_min)
print(numero_min)
print(numero_medio)
print(numero_max)
										