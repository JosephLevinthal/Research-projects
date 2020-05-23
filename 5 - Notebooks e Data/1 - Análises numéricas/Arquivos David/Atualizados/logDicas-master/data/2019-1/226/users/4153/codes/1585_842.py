# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
numero=int(input("Insira um numero inteiro de quatro digitos: "))
num1=numero//1000
num2=numero//100-(10*num1)
num3=numero//10-(numero//100)*10
num4=numero%num3

print(num1+num2+num3+num4)
