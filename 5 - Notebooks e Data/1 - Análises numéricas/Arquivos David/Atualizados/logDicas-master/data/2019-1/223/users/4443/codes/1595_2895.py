# Leitura das entradas da quantidade de jogos e conversao para int:
njogos = int(input("Quantos jogos a serem encomendados? "))

# Leitura do valor das entradas e conversao para float:
var = float(input("Qual o valor unitario de cada jogo? "))

# Leitura do valor do frete e conversao para int:
frete = float(input("Qual o valor do frete? "))

# Calculo do valor a ser pago, incluindo o frete:
total = (var*njogos) + frete

# Impressao do valor total:
print(total)