# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = int(input("numero a: "))
b = int(input("numero b: "))
c = int(input("numero c: "))
print(min(a,b,c),a+b+c-min(a,b,c)-max(a,b,c),max(a,b,c))
