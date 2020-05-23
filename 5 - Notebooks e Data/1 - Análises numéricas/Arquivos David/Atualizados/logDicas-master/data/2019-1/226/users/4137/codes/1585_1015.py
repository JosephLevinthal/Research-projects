# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = int(input("Escreva o primeiro numero:"))
b = int(input("Escreva o segundo numero:"))
c = int(input("Escreva o terceiro numero:"))
mini = min(a, b, c)
maxi = max(a, b ,c)
inte = (a+b+c - mini - maxi)
print(mini)
print(inte)
print(maxi)