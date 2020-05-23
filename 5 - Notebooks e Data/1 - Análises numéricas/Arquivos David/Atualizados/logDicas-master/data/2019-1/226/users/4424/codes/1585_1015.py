# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
numero1=int(input("digite o 1 numero "))
numero2=int(input("digite o 2 numero"))
numero3=int(input("digite o 3 numero"))

x=min(numero1,numero2,numero3)
z=max(numero1,numero2,numero3)
y=numero1+numero2+numero3-x-z

print(x,y,z)