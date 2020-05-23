# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.
valor = int(input("Qual o valor do saque? "))
x=valor//100
r=valor-(x*100)
y=r//50
r2=valor-((y*50)+(x*100))
z=r2//10

print(int(x))
print(int(y))
print(int(z))