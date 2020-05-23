qtde_jogos = int(input("Qual a quantidade de jogos a serem encomendados? "))
valor_unit = float(input("Qual o valor unitario de cada jogo? "))
valor_frete = float(input("Qual o valor do frete? "))

total = (valor_unit * qtde_jogos) + valor_frete

print(total)