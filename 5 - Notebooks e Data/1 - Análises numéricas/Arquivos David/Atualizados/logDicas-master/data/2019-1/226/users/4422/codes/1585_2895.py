quantidade = (float(input("Quantos jogos? ")))
valor = (float(input("Qual o valor unitario do jogo? ")))
frete = (float(input("Qual o valor do frete? ")))

precot = int(quantidade * valor + frete)
print(precot)