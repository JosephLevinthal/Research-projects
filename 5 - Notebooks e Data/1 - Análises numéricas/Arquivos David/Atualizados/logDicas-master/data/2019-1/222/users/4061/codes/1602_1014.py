# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

#totalvenda recebe um numero que vai tirar 30%
#saida vai imprimir só o lucro

#var totalvenda
totalvenda = float(input("Digite o total de valor da linha de cosmeticos: "))
lucro = float((totalvenda/100)*30)
print(round(lucro,2))