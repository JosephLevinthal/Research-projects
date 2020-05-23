# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
num = int(input("numero inteiro quatro digitos: "))
num1 = num//1000
num2 = (num//100) % 10 
num3 = (num//10) % 10 
num4 = num % 10
soma = num1 + num2 + num3 + num4
print(soma)
