# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a= int(input("digite a:"))
b= int(input("digite b:"))
c= int(input("digite c:"))

menorvalor = min(a,b,c)
maiorvalor = max(a,b,c)
intermediario = a+b+c-menorvalor-maiorvalor

print(menorvalor)
print(intermediario)
print(maiorvalor)


