# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
numero1=int(input("Insira um numero inteiro: "))
numero2=int(input("Insira um numero inteiro: "))
numero3=int(input("Insira um numero inteiro: "))

menor=min(numero1,numero2,numero3)
maior=max(numero1,numero2,numero3)
medio=((numero1+numero2+numero3)-menor)-maior

print(menor)
print(medio)
print(maior)