#definimos a quantidade de jogos por site
qjogos=float(input("quantidade de jogos por site"))
#definimos a variavel do valor do jogo
valor_jogo=float(input("valor do jogo por site"))
#definimos a variavel do frete
valor_frete=float(input("valor frete por site"))
#definimos a variavel do total a pagar
total=float((qjogos*valor_jogo)+valor_frete)
#imprimimos o resultado
print(total)