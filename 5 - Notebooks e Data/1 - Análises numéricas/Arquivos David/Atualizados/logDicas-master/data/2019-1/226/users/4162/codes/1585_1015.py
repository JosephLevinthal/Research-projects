# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
numero1=int(input("digite o numero: "))
numero2=int(input("digite o numero: "))
numero3=int(input("digite o numero: "))
first=min(numero1,numero2,numero3)
third=max(numero1,numero2,numero3)
second= (numero1+numero2+numero3) - first - third
print(first)
print(second)
print(third)