# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.
quantidade = int(input("A quantidade de jogos a serem encomendados? "))
# Leitura das entradas e conversao para float:
var = float(input("O valor unitario de cada jogo? "))
frete = float(input("O valor do frete? "))
# Calculo do valor a ser pago, incluindo o frete:
total = frete + (var*quantidade)

# Impressao do valor total:
print(total)