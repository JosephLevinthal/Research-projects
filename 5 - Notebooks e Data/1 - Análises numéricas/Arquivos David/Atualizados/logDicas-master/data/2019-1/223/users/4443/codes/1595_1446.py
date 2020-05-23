# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

# Leitura do valor das entradas de litros e conversao para float:
var = float(input("Quantos litros foram comprados? "))

# Quantidade que pertence a Michael
mch = round(var*1/3, 3)
print(mch)
